Param(
    [string]$StackName = "ZeldaEC2Stack",
    [string]$InstanceType = "t2.micro",
    [string]$KeyName = "myKeyPair",
    [string]$Environment = "dev"
)

# First, run cfn-lint to catch any silly typos or style issues before I bother AWS.
Write-Host "Linting the CloudFormation template..."
cfn-lint .\IaC\ec2-instance.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "Lint failed. Oops, gotta fix the template first!"
    exit 1
}

# Validate the template with AWS to ensure it's legit CloudFormation.
Write-Host "Validating template with AWS..."
aws cloudformation validate-template --template-body file://IaC/ec2-instance.yaml
if ($LASTEXITCODE -ne 0) {
    Write-Host "AWS validation failed. Check errors and try again."
    exit 1
}

Write-Host "Template looks good. Let's deploy now..."
aws cloudformation deploy `
    --template-file IaC/ec2-instance.yaml `
    --stack-name $StackName `
    --parameter-overrides InstanceType=$InstanceType KeyName=$KeyName Environment=$Environment `
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

if ($LASTEXITCODE -ne 0) {
    Write-Host "Deployment failed! Maybe check parameters or permissions."
    exit 1
} else {
    Write-Host "Deployment done! Running 'wait' command to ensure stack is fully created..."
}

# Wait until stack creation is complete so I know it's actually ready.
aws cloudformation wait stack-create-complete --stack-name $StackName
Write-Host "Stack creation complete! You can describe the stack for outputs or just test in a browser."
