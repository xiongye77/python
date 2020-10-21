pip install Faker when code require from faker import Faker


[ec2-user@ip-192-168-23-47 sqs]$ python3
Python 3.7.9 (default, Aug 27 2020, 21:59:41)
[GCC 7.3.1 20180712 (Red Hat 7.3.1-9)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> exit()
[ec2-user@ip-192-168-23-47 sqs]$ python3 send_message.py




#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import argparse
import logging
import sys
from time import sleep

import boto3
from faker import Faker

parser = argparse.ArgumentParser()
parser.add_argument("--queue-name", "-q", required=True,
                    help="SQS queue name")
parser.add_argument("--interval", "-i", required=True,
                    help="timer interval", type=float)
parser.add_argument("--message", "-m", help="message to send")
parser.add_argument("--log", "-l", default="INFO",
                    help="logging level")
args = parser.parse_args()

if args.log:
    logging.basicConfig(
        format='[%(levelname)s] %(message)s', level=args.log)

else:
    parser.print_help(sys.stderr)

sqs = boto3.client('sqs')

response = sqs.get_queue_url(QueueName=args.queue_name)
print("response is ",response)
# {'QueueUrl': 'https://ap-south-1.queue.amazonaws.com/207880003428/Messages', 'ResponseMetadata': {'RequestId': 'c7abc22f-48e0-5798-85a0-9a2779918866', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'c7abc22f-48e0-5798-85a0-9a2779918866', 'date': 'Tue, 20 Oct 2020 00:28:33 GMT', 'content-type': 'text/xml', 'content-length': '331'}, 'RetryAttempts': 0}}

queue_url = response['QueueUrl']

logging.info(queue_url)
#[INFO] https://ap-south-1.queue.amazonaws.com/207880003428/Messages

while True:
    message = args.message
    if not args.message:
        fake = Faker()
        message = fake.text()

    logging.info('Sending message: ' + message)

    response = sqs.send_message(
        QueueUrl=queue_url, MessageBody=message)

    logging.info('MessageId: ' + response['MessageId'])
    sleep(args.interval)
    
    
[INFO] Sending message: Report themselves source series single shoulder talk. Our major decision eight.
[INFO] MessageId: 63f642ec-0b3f-4b38-a483-d27ec636ea23



AWS lambda code as 


import json
import os
from datetime import datetime
import logging
logger = logging.getLogger(__name__)

import boto3
from botocore.exceptions import ClientError

QUEUE_NAME = os.environ['QUEUE_NAME']
MAX_QUEUE_MESSAGES = os.environ['MAX_QUEUE_MESSAGES']
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']

sqs = boto3.resource('sqs')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE)

def lambda_handler(event, context):

    # Receive messages from SQS queue
    queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

    #print("ApproximateNumberOfMessages:",
    #      queue.attributes.get('ApproximateNumberOfMessages'))
    
    #response = queue.receive_messages(MaxNumberOfMessages=1)
    try:
        for message in queue.receive_messages(MaxNumberOfMessages=2):
    
            print(message.body)
    
            response = table.put_item(
                Item={
                'MessageId': message.message_id,
                'Body': message.body,
                'Timestamp': datetime.now().isoformat()
                }
            )
            print("Wrote message to DynamoDB:", json.dumps(response))

            # Delete SQS message
            print("Deleted message:", message.message_id)
            message.delete()
        
    except ClientError as error:
        logger.exception("Couldn't receive messages from queue: %s", queue)
        raise error
    #receipt_handle = message['ReceiptHandle']
    #sqs.delete_message(
    #    QueueUrl="https://ap-south-1.queue.amazonaws.com/207880003428/Messages",
    #    ReceiptHandle=receipt_handle
    #)
