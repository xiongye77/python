import boto3
client = boto3.client('ec2', region_name='ap-southeast-2')
import time
ec2_instance_id_list=[]

def unique(list1):

    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    for x in unique_list:
        ec2 = boto3.resource('ec2',region_name='ap-southeast-2')
        ec2instance = ec2.Instance(x)
        for tags in ec2instance.tags:
            if tags["Key"] == 'Name':
                instancename = tags["Value"]
                print (x,instancename)
volumes = client.describe_volumes(Filters=[{"Name":"encrypted", "Values":["false"]}])
for volume in volumes["Volumes"]:
    if  volume.get('State')=='in-use':
        ec2_instance_id_list.append(volume["Attachments"][0].get('InstanceId'))

        print(volume["VolumeId"],volume["AvailabilityZone"],volume["State"], volume["Size"], volume["Attachments"][0].get('InstanceId'),volume["VolumeType"],
volume["Attachments"][0].get('Device'))
    #snapshot = client.create_snapshot(VolumeId=volume["VolumeId"], Description='EBS Backup {0}'.format(time))
    #print (volume["VolumeId"], snapshot.SnapshotId)
print ('\n'.join(ec2_instance_id_list))


print ("After unique sort")

unique(ec2_instance_id_list)
