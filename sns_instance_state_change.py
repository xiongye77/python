import boto3
import json

def lambda_handler(event, context):
    print ('LogEC2InstanceStateChange')
    
    sns = boto3.client("sns")
    print(json.dumps(event))
    response = sns.publish(
        TopicArn = "arn:aws:sns:ap-south-1:207880003428:Instance_State_Changed",
        Message = json.dumps(event),
        Subject = "EC2 instance state change"
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful')
    }

  

  Event triggered by Eventbridge  EC2 instance state change it will send email to SNS target which subscribe the topic 
