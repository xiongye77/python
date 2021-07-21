import json
import awswrangler as wr
from datetime import datetime
import uuid 

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print (bucket_name)
    print (key)
    read_command = "s3://{}/{}" .format(bucket_name, key)
    df = wr.s3.read_csv(read_command, dataset=False)
    
    df = df [["CUSTOMERNAME","EMAIL"]]
    print (df)
    uuid_id_id = uuid.uuid1()
    #write_command = "s3://{}/output/mydata{}.csv".format(bucket_name,uuid_id_id)
    #wr.s3.to_csv(df,write_command)
    
    write_command = "s3://{}/output/mydata{}.parquet".format(bucket_name,uuid_id_id)
    wr.s3.to_parquet(df,write_command)
    
    print (write_command)
    return {
        'statusCode': 200,
        'body': json.dumps('Successful')
    }
