# Zelda Musical Soundscapes

This project provides a feature for a Zelda-like game, generating musical soundscapes within certain environments. 
Players can interact with these soundscapes to unlock items or lore through sound-based challenges.

## Features
- Dynamic sound generation based on environmental context.
- Planned integration with AWS for deployment testing (using CloudFormation).
- Unit and performance tests for reliability.

## Getting Started
- Clone this repository.
- Follow the instructions for setup and deployment.

## Infrastructure Deployment

I am providing a CloudFormation template in `IaC/ec2-instance.yaml`.
To deploy the stack, run:

##powershell
.\IaC\deploy.ps1 -StackName ZeldaEC2Stack -InstanceType t2.micro

## Testing
Use `pytest` to run unit tests:
##powershell
pytest

<<<<<<< HEAD
## Documentation

I use `pdoc` to auto-generate documentation from docstrings in our Python code.
- Run `pdoc soundscapes --output-dir docs` to regenerate docs locally.
- Check `docs/index.html` to view the documentation in your browser.

In CI, the docs are generated on each push. You can download the docs artifact from the GitHub Actions run to verify changes without leaving your browser.
=======
Documentation
Auto-generated docs are located in the docs/ folder. 
You can open docs/soundscapes/index.html in a browser to read about the feature logic.

## Overview
This repository demonstrates a professional Infrastructure as Code solution with:
- **CloudFormation** templates (EC2, S3) fully parameterized for dev/prod.
- **Unit tests & Performance tests** (Pytest).
- **Security scanning** with bandit.
- **Auto docs** with pdoc.
- **CI/CD with GitHub Actions**: linting, validation, testing, doc generation.
- **Dependabot** for dependency updates.
>>>>>>> ef43be7 (feat: Finalize infrastructure, add performance tests, bandit security checks, docs, and CI updates for eu-west-1)
