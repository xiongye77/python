import boto3
import time
S3_OUTPUT = f's3://airflow-dev-codepipeline-artifacts-babylon/result1/'
RETRY_COUNT = 10
client = boto3.client('athena')

query = f"""
        select * from "csv-to-parquet"."csv" limit 10
        """
response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={ 'Database': "csv-to-parquet" },
        ResultConfiguration={'OutputLocation': S3_OUTPUT}
    )
query_execution_id = response['QueryExecutionId']

    # Get Execution Status
for i in range(0, RETRY_COUNT):
        # Get Query Execution
    query_status = client.get_query_execution(
            QueryExecutionId=query_execution_id
    )
    exec_status = query_status['QueryExecution']['Status']['State']
    if exec_status == 'SUCCEEDED':
        print(f'Status: {exec_status}')
        break
    elif exec_status == 'FAILED':
        raise Exception(f'STATUS: {exec_status}')
    else:
        print(f'STATUS: {exec_status}')
        time.sleep(i)


result = client.get_query_results(QueryExecutionId=query_execution_id)

print(result['ResultSet']['Rows'])
