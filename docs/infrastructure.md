# Infrastructure Documentation

## Overview
This sets up a simple EC2 instance for the Zelda Soundscapes project. Basically, it's a tiny server with a webpage, so I can test concepts quickly.

## Files
- `IaC/ec2-instance.yaml`: My main CloudFormation template. It creates an EC2 instance, a security group, and sets up user data to install a web server.
- `IaC/deploy.ps1`: A PowerShell script that checks the template (lint + validate) before deploying. It also waits for the stack to be fully created.
  
## Parameters
- **InstanceType:** EC2 size. `t2.micro` is super cheap and okay for dev.
- **KeyName:** Your AWS key pair name if you want to SSH in. Make sure you have one set up in AWS first!
- **Environment:** `dev` or `prod`. Right now, it just changes the name tag and a greeting on the webpage, but you could use this to scale up resources or lock down security in the future.

## How to Deploy
1. `aws configure` to set your AWS creds if not done yet.
2. From your project root:
   ```powershell
   .\IaC\deploy.ps1 -StackName ZeldaEC2Stack -InstanceType t2.micro -KeyName MyKey -Environment dev
