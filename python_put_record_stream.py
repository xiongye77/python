import sys
import json
import boto3
import random
import datetime
import pandas as pd

def getReferrer():
    x = random.randint(1,5)
    x = x*50
    y = x+30
    data = {}
    data['user_id'] = str(random.randint(x,y))
    data['device_id'] = random.choice(['mobile','computer', 'tablet', 'mobile','computer', 'voice', 'AI-ML'])
    data['client_event'] = random.choice(['auto_nav','product_checkout','electronics_product_detail',
    'electronics_products','electronics_selection','electronics_cart'])
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['client_timestamp'] = str_now
    return data

kinesis = boto3.client('kinesis', region_name='ap-south-1')
number_of_records = 200
record_count = 0
while record_count < number_of_records:
    data = json.dumps(getReferrer())
    print(data)
    kinesis.put_record(
            StreamName='testt',
            Data=data,
            PartitionKey='partitionkey')
    record_count += 1

    
    
    
    
  Put clickstream data to Kinesis data stream and use Firehose change from json to parquet. use Athena to query those data 
  
  
  CREATE EXTERNAL TABLE default.clickstream (
  user_id string,
  device_id string,
  client_event string,
  client_timestamp string
  )
  STORED AS parquet
  LOCATION 's3://clickstreamfilestore1478/'
  TBLPROPERTIES ("parquet.compression"="SNAPPY")
