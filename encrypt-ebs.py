# encrypt one-EC2 instance all uncrupted volumes 
import time
from time import gmtime, strftime
import boto3
import botocore
import sys
client = boto3.client('ec2', region_name='ap-southeast-2')
#print 'Number of arguments:', len(sys.argv), 'arguments.'
if len(sys.argv) > 2:
    print ('only one instance id is needed,program exit')
    exit(0)

instance_id_handle=str(sys.argv[1])

print (" We are handleing instance  ({})" .format(instance_id_handle))
instance = client.describe_instances(Filters=[{'Name': 'instance-id', 'Values': [instance_id_handle]}])

client.stop_instances(InstanceIds=[instance_id_handle])
waiter_instance_stopped = client.get_waiter('instance_stopped')
waiter_instance_stopped.wait(InstanceIds=[instance_id_handle])

print('Instance stopped')

volumes = client.describe_volumes(Filters=[{"Name":"encrypted", "Values":["false"]},{"Name":"attachment.instance-id","Values":[instance_id_handle]}])
for volume in volumes["Volumes"]:
    ctime = strftime("%a, %d %b %Y %X +0000", gmtime())
    client.detach_volume(InstanceId=volume["Attachments"][0].get('InstanceId'),VolumeId=volume["VolumeId"],Force=True,Device=volume["Attachments"
][0].get('Device'))
    print (volume["VolumeId"])

    client.get_waiter('volume_available').wait(VolumeIds=[volume["VolumeId"]])

    print ("Volume detach finished")
    #print(volume["VolumeId"])
    snapshot = client.create_snapshot(VolumeId=volume["VolumeId"], Description='EBS Backup {0}'.format(ctime))
    snapshot_id = snapshot['SnapshotId']
    print (volume["VolumeId"],snapshot_id)
    try:
        snapshot_complete_waiter= client.get_waiter('snapshot_completed')
        snapshot_complete_waiter.wait(SnapshotIds=[snapshot_id])
    #except:
    except botocore.exceptions.WaiterError as e:
        print(e)
    print ("Create snapshot finished ({})" .format(snapshot_id))
    #volume_id_list=[]
    #for item in instance.volumes.all():
    #volume_id_list.append(item.id)
    copied_snapshot=client.copy_snapshot(SourceSnapshotId=snapshot_id,SourceRegion='ap-southeast-2',KmsKeyId='a02dfc64-b9cf-4f64-8055-96c3551077d5',Encrypted
=True)
    copy_snapshot_id = copied_snapshot['SnapshotId']
    print (copied_snapshot)
    try:
        snapshot_complete_waiter= client.get_waiter('snapshot_completed')
        snapshot_complete_waiter.wait(SnapshotIds=[copy_snapshot_id])
    #except:
    except botocore.exceptions.WaiterError as e:
        print(e)
    print ("Copy snapshot finished new snapshot id ({})" .format(copy_snapshot_id))
    new_volume=client.create_volume(Size=volume["Size"],VolumeType=volume["VolumeType"],AvailabilityZone=volume["AvailabilityZone"],SnapshotId=copy_snapshot_
id)
    print (new_volume)
    client.get_waiter('volume_available').wait(VolumeIds=[new_volume['VolumeId']])
    print ("New volume create finished volume id  ({})" .format(new_volume['VolumeId']))

    client.attach_volume(Device=volume["Attachments"][0].get('Device'),InstanceId=volume["Attachments"][0].get('InstanceId'),VolumeId=new_volume['VolumeId'])
    client.get_waiter('volume_in_use').wait(VolumeIds=[new_volume['VolumeId']])
    print ("Attach finished")


client.start_instances(InstanceIds=[instance_id_handle])
