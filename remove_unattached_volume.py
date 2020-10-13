import boto3


#def lambda_handler(object, context):

    # Get list of regions
ec2_client = boto3.client('ec2')
regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)
    print("Region:", region)

        # List only unattached volumes ('available' vs. 'in-use')
    volumes = ec2.volumes.filter(
            Filters=[{'Name': 'status', 'Values': ['available']}])

    for volume in volumes:
        v = ec2.Volume(volume.id)
        print("Deleting EBS volume: {}, volume-type: {} Size: {} GiB Creation date {} ".format(v.id, v.volume_type ,v.size,v.create_time.strftime("%Y-%m-%d %
H:%M:%S")))
#            v.delete()
