Param(
    [string]$StackName = "ZeldaEC2Stack",
    [string]$InstanceType = "t2.micro"
)

# Deploy or update the stack
aws cloudformation deploy `
    --template-file IaC/ec2-instance.yaml `
    --stack-name $StackName `
    --parameter-overrides InstanceType=$InstanceType `
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM

Write-Host "Deployment complete. You can describe the stack with:"
Write-Host "aws cloudformation describe-stacks --stack-name $StackName"
