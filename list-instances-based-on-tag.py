import boto3

AWS_REGION = "ap-southeast-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_NAME_TAG_VALUE = 'my-ec2-instance'

instances = EC2_RESOURCE.instances.filter(
    Filters=[
        {
            'Name': 'tag:ClusterName',
            'Values': [
                'ES-APM'
            ]
        }
    ]
)

print(f'Instances with Tag "Name={INSTANCE_NAME_TAG_VALUE}":')

for instance in instances:
    print(f'  - Instance ID Instance IP: {instance.id ,instance.key_name}')

for instance in instances:
    print(f'  {instance.private_ip_address}')
