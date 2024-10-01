import json
import boto3

#Replace with your EC2 region
region = 'us-east-1'

# IDs of the instances to stop in the below list
instances = ['i-0cce988c5514d873c', 'i-0df6d5624ed347bd0','i-09ac8c4d0ac090c16']

ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: '+ str(instances))
