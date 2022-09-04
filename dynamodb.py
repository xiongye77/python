# Scan all records qualified with requirements
https://medium.com/towards-data-engineering/scan-complete-dynamodb-table-python-9f61acce4a20
  

import boto3
import botocore
from boto3.dynamodb.conditions import Attr


def scan_db(table, scan_kwargs=None):
    """
    Get all records of the dynamodb table where the FilterExpression holds true
    :param scan_kwargs: Used to pass filter conditions, know more about kwargs- geeksforgeeks.org/args-kwargs-python/
    :type scan_kwargs: dict
    :param table: dynamodb table name
    :type table: str
    :return: list of records
    :rtype: dict
    """
    if scan_kwargs is None:
        scan_kwargs = {}
    dynamodb = boto3.resource('dynamodb','ap-southeast-2')
    table = dynamodb.Table(table)

    complete = False
    records = []
    while not complete:
        try:
            response = table.scan(**scan_kwargs)
        except botocore.exceptions.ClientError as error:
            raise Exception('Error quering DB: {}'.format(error))

        records.extend(response.get('Items', []))
        next_key = response.get('LastEvaluatedKey')
        scan_kwargs['ExclusiveStartKey'] = next_key

        complete = True if next_key is None else False
    return records


if __name__ == '__main__':
    table_name = "new_offline_event"
    kwargs = {
        'FilterExpression': Attr("event_time").contains('2022-09-02')
    }
    for i in scan_db(table_name, kwargs):
        print(i['event_time'])
        
        
        
        
aws dynamodb scan   --attributes-to-get gaClientId eventName   --table-name GA_Record --query "Items[*]"  --region=ap-southeast-2   | jq --compact-output '.[]'   | tr '\n' '\0'   | xargs -0 -t -I %  aws dynamodb delete-item --table-name GA_Record --key % --region=ap-southeast-2

[ye.xiong@ip-172-31-43-214 ~]$ python3 dynamodb.py
Deleted 3102
[ye.xiong@ip-172-31-43-214 ~]$ more dynamodb.py
import boto3
dynamo = boto3.resource('dynamodb','ap-southeast-2')

def truncateTable(tableName):
    table = dynamo.Table(tableName)

    #get the table keys
    tableKeyNames = [key.get("AttributeName") for key in table.key_schema]

    #Only retrieve the keys for each item in the table (minimize data transfer)
    projectionExpression = "#g,#e "
    expressionAttrNames = {'#g':'gaClientId','#e':'eventName'}

    counter = 0
    page = table.scan(ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames)
    with table.batch_writer() as batch:
        while page["Count"] > 0:
            counter += page["Count"]
            # Delete items in batches
            for itemKeys in page["Items"]:
                batch.delete_item(Key=itemKeys)
            # Fetch the next page
            if 'LastEvaluatedKey' in page:
                page = table.scan(
                    ProjectionExpression=projectionExpression, ExpressionAttributeNames=expressionAttrNames,
                    ExclusiveStartKey=page['LastEvaluatedKey'])
            else:
                break
    print(f"Deleted {counter}")

truncateTable("GA_Record")
