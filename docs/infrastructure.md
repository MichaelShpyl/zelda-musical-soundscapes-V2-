# Infrastructure Documentation

We use AWS CloudFormation to define infrastructure as code, enabling consistent, repeatable deployments.

## EC2 Instance (ec2-instance.yaml)
- Parameters: InstanceType, KeyName, Environment.
- Environment determines tagging.
- IAM role grants S3 read-only access for future expansions.
- Outputs: InstanceId (for reference), PublicIP (connect if needed).

## S3 Bucket (s3-bucket.yaml)
- Parameters: BucketName (must be unique), Environment.
- Private bucket for secure storage.
- Output: BucketName for reference.

## Deployment Steps
Validate:
```bash
aws cloudformation validate-template --template-body file://IaC/ec2-instance.yaml --region eu-west-1
Deploy EC2 (dev):
aws cloudformation create-stack \
  --stack-name MyEC2Stack \
  --template-body file://IaC/ec2-instance.yaml \
  --parameters file://IaC/parameters-dev.json \
  --capabilities CAPABILITY_IAM \
  --region eu-west-1
Check status:
aws cloudformation describe-stacks --stack-name MyEC2Stack --region eu-west-1
Delete if no longer needed:
aws cloudformation delete-stack --stack-name MyEC2Stack --region eu-west-1
S3 Bucket example:
aws cloudformation create-stack \
  --stack-name MyS3BucketStack \
  --template-body file://IaC/s3-bucket.yaml \
  --parameters ParameterKey=BucketName,ParameterValue=my-unique-bucket-xyz123 \
               ParameterKey=Environment,ParameterValue=dev \
  --region eu-west-1