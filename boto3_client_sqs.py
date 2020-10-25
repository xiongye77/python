[cloud_user@ip-10-0-1-39 ~]$ ls -lt
total 32
-rw-r--r-- 1 root root   23 Oct 25 09:46 sqs_url.py
-rw-r--r-- 1 root root  614 Oct 25 09:46 queue_status.py
-rw-r--r-- 1 root root  123 Oct 25 09:46 purge_queue.py
-rw-r--r-- 1 root root  706 Oct 25 09:46 fifo_producer.py
-rw-r--r-- 1 root root  933 Oct 25 09:46 fifo_consumer.py
-rw-r--r-- 1 root root 5894 Oct 25 09:46 data.json
-rw-r--r-- 1 root root  338 Oct 25 09:46 create_queue.py
[cloud_user@ip-10-0-1-39 ~]$ more *.py
::::::::::::::
create_queue.py
::::::::::::::
import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='mynewq.fifo',
    Attributes={
        'DelaySeconds': '5',
        'MessageRetentionPeriod': '86400',
        'FifoQueue': 'true',
        'ContentBasedDeduplication': 'true'
    }
)

print(response['QueueUrl'])
::::::::::::::
fifo_consumer.py
::::::::::::::
import boto3
import json
import time
from sqs_url import QUEUE_URL

# Create SQS client
sqs = boto3.client('sqs')

i = 0

while i < 10000:
    i = i + 1
    rec_res = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        MessageAttributeNames=[
            'All',
        ],
        MaxNumberOfMessages=1,
        VisibilityTimeout=5,
        WaitTimeSeconds=10
    )
    time.sleep(2)
    # If our task takes too long we can't delete it
    # time.sleep(5)
    del_res = sqs.delete_message(
        QueueUrl=QUEUE_URL,
        ReceiptHandle=rec_res['Messages'][0]['ReceiptHandle']
    )
    print("RECIEVED MESSAGE:")
    print('FROM PRODUCER: ' + rec_res['Messages'][0]['MessageAttributes']['Producer']['StringValue'])
    print('JOB TYPE: ' + rec_res['Messages'][0]['MessageAttributes']['JobType']['StringValue'])
    print('BODY: ' + rec_res['Messages'][0]['Body'])
    print("DELETED MESSAGE")
    print("")
    time.sleep(1)
::::::::::::::
fifo_producer.py
::::::::::::::
import boto3
import json
import time
from sqs_url import QUEUE_URL

# Create SQS client
sqs = boto3.client('sqs')

with open('data.json', 'r') as f:
    data = json.loads(f.read())

for i in data:
    msg_body = json.dumps(i)
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=msg_body,
        MessageAttributes={
            'JobType': {
                'DataType': 'String',
                'StringValue': 'NewDonor'
            },
            'Producer': {
                'DataType': 'String',
                'StringValue': 'Default'
            }
        },
        MessageGroupId='messageGroup1'
    )
    print("Added Message:")
    print(response)
    time.sleep(1)
::::::::::::::
purge_queue.py
::::::::::::::
import boto3
from sqs_url import QUEUE_URL

sqs = boto3.client('sqs')

response = sqs.purge_queue(
    QueueUrl=QUEUE_URL
)
::::::::::::::
queue_status.py
::::::::::::::
import boto3
import time
from sqs_url import QUEUE_URL

sqs = boto3.client('sqs')

i = 0

while i < 100000:
    i = i + 1
    time.sleep(1)
    response = sqs.get_queue_attributes(
        QueueUrl=QUEUE_URL,
        AttributeNames=[
            'ApproximateNumberOfMessages',
            'ApproximateNumberOfMessagesNotVisible',
            'ApproximateNumberOfMessagesDelayed',
        ]
    )
    for attribute in response['Attributes']:
        print(
            response['Attributes'][attribute] +
            ' ' +
            attribute
        )
    print('')
    print('')
    print('')
    print('')

::::::::::::::
sqs_url.py
::::::::::::::
QUEUE_URL = 'REPLACEME'




Working with SQS FIFO Queues

In this video, you will be provided with a full walkthrough on how to create an SQS FIFO Queue using the AWS SDK for Python, 
Boto3. You will use several Python3 scripts to interact with that FIFO queue using Boto3, including sending messages into the queue, 
consuming and deleting the messages from the queue, and also monitoring the state of the queue. 


Learning Objectives
check_circle
Create a FIFO SQS Queue

You'll need to create an AWS SQS Queue using the AWS CLI on the EC2 instance provided.

    Sign in to the EC2 instance provided using the credentials in Cloud Assessments
    Run the Python script to create the SQS queue create_queue.py
    Remember to copy the URL that is printed to the screen and paste it into to the sqs_url.py file for later

check_circle
Send and Process Messages to Your SQS FIFO Queue

Use the EC2 instance provided to send messages to your SQS queue and process them.

    Make sure you've updated the sqs_url.py file with the SQS queue URL
    Review the data.json file
    Remember to start up the queue_status.py script
    Run the Python3 fifo_producer.py script to send messages to the SQS queue
    Run the Python3 fifo_consumer.py script to consume the messages in the queue
    If you need to start over at any point you can start over with the purge_queue.py script

