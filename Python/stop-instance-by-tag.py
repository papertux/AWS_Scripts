"""
#  By: David Mansfield
#  Version: 1.0.1

This script will stop instances that are running based on their Tag
"""

import boto3

#  Change to the value to the desired region.
region = 'us-east-1'

#  Change the value to match the Tag used on the instance.
tag = 'Env=dev'

#  Connect to EC2
ec2 = boto3.resource('ec2', region_name=region)

#  Check for running instances with the specific tag and stop them.
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:Name', 'Values': [tag]}])

for instance in instances:
    for tags in instance.tags:
        if tags['Key'] == 'Name':
            name = tags['Value']

    print ('Stopping instance Tagged:' + name + ' (' + instance.id + ')')
    instance.stop()
