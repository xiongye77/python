import os

import boto3


dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')
rekognition = boto3.client('rekognition')
TABLE_NAME = os.environ['TABLE_NAME']
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    obj = s3.Object(bucket, key)
    image = obj.get()['Body'].read()
    print("image",image)
    print("obj",obj)
    print('Recognizing celebrities...')
    labels = rekognition.detect_labels(Image={'Bytes': image}, MaxLabels=10)
    print("labels are ",labels)
    results = []
    
    for label in labels['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        results.append(label['Name']+str(label['Confidence']))
    
    print(results)

    print('Saving face data to DynamoDB table:', TABLE_NAME)
    
    response = table.put_item(
        Item={
            'key': key,
            'results': results,
        }
    )
