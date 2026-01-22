# AWS Lambda: Automatically Stop EC2 Instances

This project demonstrates how to use AWS Lambda and Amazon EventBridge to automatically stop EC2 instances on a scheduled basis in order to reduce unnecessary cloud costs.

The objective is to automate resource management in a development environment by shutting down EC2 instances after business hours.

## Project Goal

Automate the shutdown of EC2 instances so that:
- Cloud costs are reduced during off-hours
- Manual intervention is eliminated
- Resource management is consistent and reliable
- Automation follows a predictable schedule

## Project Scenario

A DevOps team uses multiple EC2 instances in a development lab to test application releases.  
Managers noticed increasing cloud costs due to instances being left running after work hours.

The solution is to create a serverless automation that:
- Identifies running EC2 instances
- Stops them automatically after 7:00 PM each day
- Runs without managing servers or manual scripts

## Technologies Used

- AWS Lambda
- Amazon EC2
- Amazon EventBridge (CloudWatch Events)
- IAM
- Python (Boto3)
- GitHub

## Architecture Overview

The solution includes:
- Multiple EC2 instances running in a development environment
- A Lambda function written in Python to stop EC2 instances
- IAM permissions allowing Lambda to manage EC2 resources
- An EventBridge rule that triggers the Lambda function on a daily schedule

## Prerequisites

- AWS account
- Running EC2 instances
- Basic Python knowledge
- Familiarity with AWS IAM
- GitHub account

## Project Steps

### Step 1: Prepare the EC2 Environment
- Created multiple EC2 instances to simulate a development lab
- Left the instances running to represent typical after-hours usage

### Step 2: Create the Lambda Function
- Created a new Lambda function using the Python runtime
- Selected an appropriate runtime and architecture
- Prepared the function to execute a Python script using Boto3

### Step 3: Configure IAM Permissions
- Reviewed the default Lambda execution role
- Added permissions to allow the Lambda function to stop EC2 instances
- Ensured the function had sufficient access to manage EC2 resources

### Step 4: Implement the EC2 Stop Logic
- Wrote a Python script that identifies EC2 instances
- Configured the script to stop the specified instances
- Deployed the function and tested it to confirm instances stopped successfully

### Step 5: Create an EventBridge Schedule
- Created an EventBridge rule with a scheduled trigger
- Configured the rule to run daily after business hours
- Set the Lambda function as the target for the rule

### Step 6: Verify Automation
- Confirmed the Lambda function executed at the scheduled time
- Verified EC2 instances transitioned to a stopped state
- Reviewed logs to ensure successful execution

## Results

- EC2 instances were automatically stopped after work hours
- Cloud costs were reduced by preventing unnecessary runtime
- Automation ran reliably without manual intervention
- Serverless tools were used to manage infrastructure efficiently

## Documentation

A full step-by-step walkthrough of this project, including screenshots, is available on Medium:

**AWS Lambda: Automatically Stop EC2 Instances** 

https://medium.com/@labossiere01/aws-lambda-automatically-stop-ec2-instances-05d463ca6bc2
