Step 1: Write the Python code of the Lambda function that will enforce encryption (enforce_bucket_encryption.tf)
  
  
  ###############################################
## Author : Hervekhg
## Description: This Lambda function enforce encryption on unencrypted S3 Bucket
#####################################################

from boto3 import resource, client
from logging import getLogger, info, error, debug
from os import environ
from botocore.exceptions import ClientError

SSEAlgorithm = "aws:kms"
KMSMasterKeyID = environ['KMSMasterKeyID'] 

class Enforce_EBS_Encryption(object):

    def __init__(self):
        
        self.s3_client = client('s3')
        
        self.logger = getLogger()
        self.logger.setLevel("INFO")
        self.unencryptedbucket = list()

    def getlistofUnEncryptedBucket(self):
        response = self.s3_client.list_buckets()
        for bucket in response['Buckets']:
            try:
                resp_encryption = self.s3_client.get_bucket_encryption(
                    Bucket=bucket['Name']
                )
                rules = resp_encryption['ServerSideEncryptionConfiguration']['Rules']
                info("{0} is already encrypted : Encryption : {1}".format(bucket['Name'],rules))
            except ClientError as e:
                if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                    info("{0} is not encrypted but will be, No Encrytion found".format(bucket['Name']))
                    self.unencryptedbucket.append(bucket['Name'])
                else:
                    error("Unexpected error on Bucket: {0}".format(bucket['Name']))
    
    def _putEncryptiononSingleBucket(self,bucket_name):
        resp = self.s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': SSEAlgorithm,
                            'KMSMasterKeyID': KMSMasterKeyID
                        }
                    },
                ]
            }
        )
    
    def forceEncrytionOnUnEncryptedBucket(self):
        for bucket in self.unencryptedbucket:
            self._putEncryptiononSingleBucket(bucket)
            info("The Bucket : {0} has been encrypted with KMS key".format(bucket))
            

def lambda_handler(event, context):
    print("***** Start Processing ****")
    s3_encryption = Enforce_EBS_Encryption()
    s3_encryption.getlistofUnEncryptedBucket()
    s3_encryption.forceEncrytionOnUnEncryptedBucket()
    print("***** End Processing ****")
    
    
    
    
Step 2: Declare all variables (var.tf)


variable "lambda_s3_bucket" {
  type    = string
  default = "BUCKET-THAT-CONTAIN-LAMBDAZIPCODE"
}

variable "kms_key_id" {
  type = string
  default = "KMSKEY-ARN3"
}

variable "cron_schedule_enforce_bucket_encryption" {
  type = string
  default = "cron(0 11,19 ? * * *)"
}

variable "sns_topic_arn" {
  type = string
  default = "SNSTOPICARN"
}




Step 3: Create a policy document for lambda function (policy_doc.tf)
  
  data "aws_iam_policy_document" "lambda_policy_doc" {
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
      "config:PutEvaluations",
    ]

    resources = [
      "*",
    ]
  }
  
  statement {
    effect = "Allow"
    actions = [
      "s3:ListBuckets",
      "s3:ListAllMyBuckets",
      "s3:GetBucketEncryption",
      "s3:GetEncryptionConfiguration",
      "s3:PutEncryptionConfiguration",
    ]
    resources = [
      "*"
    ]
  }
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = [
      "sts:AssumeRole",
    ]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}




Step 4: Create policy an attach to a role (iam_policies.tf)
  resource "aws_iam_policy" "lambda_policy" {
  name   = aws_iam_role.force_bucket_encryption.name
  path   = "/"
  policy = data.aws_iam_policy_document.lambda_policy_doc.json
}

resource "aws_iam_role_policy_attachment" "ec2_tags_enforced" {
  role       = aws_iam_role.force_bucket_encryption.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}


Step 5: Create a lambda function and its role
  
  
  
  resource "aws_lambda_layer_version" "dep" {
  layer_name = "force_bucket_encryption"
  s3_bucket  = var.lambda_s3_bucket
  s3_key     = "force_bucket_encryption/lib.zip"

  compatible_runtimes = ["python3.6"]
}

resource "aws_lambda_function" "force_bucket_encryption" {
  s3_bucket     = var.lambda_s3_bucket
  s3_key        = "force_bucket_encryption/lambdacode.zip"
  function_name = "force_bucket_encryption"
  role          = aws_iam_role.force_bucket_encryption.arn
  handler       = "force_bucket_encryption.lambda_handler"
  runtime       = "python3.6"
  memory_size   = 128
  timeout       = 300

  layers = [
    aws_lambda_layer_version.dep.arn,
  ]
  environment{
    variables = {
      KMSMasterKeyID = var.kms_key_id
    } 
  } 
}

resource "aws_iam_role" "force_bucket_encryption" {
  name        = "lambda_force_bucket_encryption"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}



Step 6: Create Cloudwatch Event Rule
  resource "aws_cloudwatch_event_rule" "daily" {
  name        = "daily_enforce_bucket_kms_encryption"
  description = "run everyday"

  #schedule_expression = "${var.cron_schedule_enforce_bucket_encryption} "
  event_pattern = <<PATTERN
  {
    "source": [
      "aws.s3"
    ],
    "detail-type": [
      "AWS API Call via CloudTrail"
    ],
    "detail": {
      "eventSource": [
        "s3.amazonaws.com"
      ],
      "eventName": [
        "CreateBucket"
      ]
    }
  }
  PATTERN

}
  
  
  Step 7: Create Cloudwatch Event target for executing Lambda
    
 resource "aws_cloudwatch_event_target" "target_lambda" {
  rule      = aws_cloudwatch_event_rule.daily.name
  target_id = "enforce_bucket_kms_encryption"
  arn       = aws_lambda_function.force_bucket_encryption.arn
 }



Step 8: Create Cloudwatch Event target for sending SNS Notifications
  
  resource "aws_cloudwatch_event_target" "sns_target" {
  arn = var.sns_topic_arn
  rule = aws_cloudwatch_event_rule.daily.name
  target_id = "send-sns-notification"
}
  
