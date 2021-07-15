
[ec2-user@ip-192-168-23-47 python]$ rm -rf *
[ec2-user@ip-192-168-23-47 python]$ pip install pymysql==0.10.1 -t .
Collecting pymysql==0.10.1
  Using cached PyMySQL-0.10.1-py2.py3-none-any.whl (47 kB)
Installing collected packages: pymysql
Successfully installed pymysql-0.10.1

[ec2-user@ip-192-168-23-47 temp]$ pip list  |grep -i  mysql
mysql-connector-python                   8.0.25
PyMySQL                                  0.10.1


[ec2-user@ip-192-168-23-47 python]$ ls -lt
total 0
drwxrwxr-x 2 ec2-user ec2-user 135 Jul 15 07:15 PyMySQL-0.10.1.dist-info
drwxrwxr-x 4 ec2-user ec2-user 279 Jul 15 07:15 pymysql
[ec2-user@ip-192-168-23-47 python]$ cd ..
[ec2-user@ip-192-168-23-47 temp]$ zip -r9 ../pymysql.zip .
updating: python/ (stored 0%)
updating: python/pymysql/ (stored 0%)
updating: python/pymysql/__init__.py (deflated 59%)
updating: python/pymysql/_auth.py (deflated 68%)
updating: python/pymysql/charset.py (deflated 83%)
updating: python/pymysql/connections.py (deflated 75%)
updating: python/pymysql/converters.py (deflated 74%)
updating: python/pymysql/cursors.py (deflated 72%)
updating: python/pymysql/err.py (deflated 61%)
updating: python/pymysql/optionfile.py (deflated 59%)
updating: python/pymysql/protocol.py (deflated 72%)
updating: python/pymysql/times.py (deflated 58%)
updating: python/pymysql/constants/ (stored 0%)
updating: python/pymysql/constants/CLIENT.py (deflated 50%)
updating: python/pymysql/constants/COMMAND.py (deflated 56%)
updating: python/pymysql/constants/CR.py (deflated 66%)
updating: python/pymysql/constants/ER.py (deflated 63%)
updating: python/pymysql/constants/FIELD_TYPE.py (deflated 45%)
updating: python/pymysql/constants/FLAG.py (deflated 31%)
updating: python/pymysql/constants/SERVER_STATUS.py (deflated 50%)
updating: python/pymysql/constants/__init__.py (stored 0%)
updating: python/pymysql/constants/__pycache__/ (stored 0%)
updating: python/pymysql/constants/__pycache__/CLIENT.cpython-38.pyc (deflated 33%)
updating: python/pymysql/constants/__pycache__/COMMAND.cpython-38.pyc (deflated 41%)
updating: python/pymysql/constants/__pycache__/CR.cpython-38.pyc (deflated 51%)
updating: python/pymysql/constants/__pycache__/ER.cpython-38.pyc (deflated 56%)
updating: python/pymysql/constants/__pycache__/FIELD_TYPE.cpython-38.pyc (deflated 33%)
updating: python/pymysql/constants/__pycache__/FLAG.cpython-38.pyc (deflated 26%)
updating: python/pymysql/constants/__pycache__/SERVER_STATUS.cpython-38.pyc (deflated 37%)
updating: python/pymysql/constants/__pycache__/__init__.cpython-38.pyc (deflated 22%)
updating: python/pymysql/__pycache__/ (stored 0%)
updating: python/pymysql/__pycache__/__init__.cpython-38.pyc (deflated 42%)
updating: python/pymysql/__pycache__/_auth.cpython-38.pyc (deflated 47%)
updating: python/pymysql/__pycache__/charset.cpython-38.pyc (deflated 64%)
updating: python/pymysql/__pycache__/connections.cpython-38.pyc (deflated 54%)
updating: python/pymysql/__pycache__/converters.cpython-38.pyc (deflated 59%)
updating: python/pymysql/__pycache__/cursors.cpython-38.pyc (deflated 55%)
updating: python/pymysql/__pycache__/err.cpython-38.pyc (deflated 54%)
updating: python/pymysql/__pycache__/optionfile.cpython-38.pyc (deflated 40%)
updating: python/pymysql/__pycache__/protocol.cpython-38.pyc (deflated 59%)
updating: python/pymysql/__pycache__/times.cpython-38.pyc (deflated 47%)
  adding: python/pymysql/_compat.py (deflated 50%)
  adding: python/pymysql/_socketio.py (deflated 67%)
  adding: python/pymysql/util.py (deflated 36%)
  adding: python/pymysql/__pycache__/_compat.cpython-38.pyc (deflated 25%)
  adding: python/pymysql/__pycache__/_socketio.cpython-38.pyc (deflated 50%)
  adding: python/pymysql/__pycache__/util.cpython-38.pyc (deflated 34%)
  adding: python/PyMySQL-0.10.1.dist-info/ (stored 0%)
  adding: python/PyMySQL-0.10.1.dist-info/LICENSE (deflated 41%)
  adding: python/PyMySQL-0.10.1.dist-info/METADATA (deflated 61%)
  adding: python/PyMySQL-0.10.1.dist-info/WHEEL (deflated 14%)
  adding: python/PyMySQL-0.10.1.dist-info/pbr.json (stored 0%)
  adding: python/PyMySQL-0.10.1.dist-info/top_level.txt (stored 0%)
  adding: python/PyMySQL-0.10.1.dist-info/RECORD (deflated 57%)
  adding: python/PyMySQL-0.10.1.dist-info/INSTALLER (stored 0%)
  adding: python/PyMySQL-0.10.1.dist-info/REQUESTED (stored 0%)
  adding: mysql2.py (deflated 39%)
  adding: mysql.py (deflated 38%)
[ec2-user@ip-192-168-23-47 temp]$ aws lambda publish-layer-version --layer-name pymysql \
>      --description "pymysql for mysql access" \
>      --zip-file fileb://../pymysql.zip \
>      --compatible-runtimes python3.8
{
    "Content": {
        "Location": "https://awslambda-ap-s-1-layers.s3.ap-south-1.amazonaws.com/snapshots/207880003428/pymysql-1654143b-c093-4457-900e-fb31f65d3a28?versionId=Tnxu8RUVE3fK_VpKj2g1yhILhYf1y1ZD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCmFwLXNvdXRoLTEiRzBFAiBWpy1A1THCYn5KNdIKtX0Mu1i8ZvWC5SHZ5D4HQcZmmgIhAKc%2FyuBJiyzeWhWzcnZeQMGJAKd53AVDkr5FdKfa9S%2BMKvwDCCYQAhoMNTQ1MjU1MjAxMzA3Igwp3SwY9a%2BQ6qiMCmIq2QPtolu75F4qGTbnPAe925AZXCuDyj7BVpS1wFxroUPDbvbSBDK7h9qiPWpy2BkyBJcaV9dqvsIVYhMfayw5Z9No6Z8g%2BgQLWkj0y3Zdmr3WlbH4oWr5fXvix7kT%2F2XVRne0Eih1NvbF1QzPbRNgthkIwaw2DaaOoaPNKIBeJ5VU6RUa9b9ConiSdyUPtxgzYPUgVWEdOqK3wuV0Ufw3ZH1zzFNCPkqBT3XoAfVMVMTvqlqw4v3OE8misjkOreHMzLMKn9xkHO6TC%2BQzsBtdc3yHRMr8bz68%2FUq9Qj4psT5A%2Bax0Usm4mW%2F5Jmx3GQvPSCWPiXq83QishG7O0zuLCb6SzUAxLf6s%2FGV31htT6am20RqBmhHVe%2Fq%2B6LuOvUUxzBcxGtNJ5cHIfiXn8kCNkDztbPZEpwq3CH9SUXKIT%2FbzRggVzOi5JSfbfFiMlwyZufiWkuAk13dM11Dn0oaIFlWhPSRvxvq4noP2f%2Bdk66ILzds0mlDvorO%2Be8s%2BMafmEnVBrM6KNmBvVtluaxQaKEf4J2sd4njBnc4YN3PJbYUHI2LE48FmDRgijKkZbNzVfMQytECOYeKUc5qTU44Wsk%2B9R6%2FbXuW7CdVtuUei%2BjkwkJhY3q%2BIUIy6vjD6kr%2BHBjqlAcvLwDRJXnXgRYNE6Z%2FdlzGlF3edaIB4FzQfbRfMXtu%2BwvHW6tYoLtSB5t8AHAfPHJCFTSEqQjPbepGHwGA8w3Z4gyZOGVmZ%2FY8LtjUU5e8iaKdKIP87cb9pmgkB%2BytMsoo2fi7yjPL3ONxAXlcYDE2WJ0R7r1XjrlDmygXOBiMGYuat5NRRIWTng9iK%2BfpWz7FE75wchpBAu2zFWlsDPZhTD7j1gg%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210715T071546Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIAX5456DIN23GVTON4%2F20210715%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=b85df0b46bacc945511ba97ab3b4621c6f6d7679850d65dc148ba01ac428d33d",
        "CodeSha256": "PSFSOUcNwSTvfBCQ0yI3UFdHzxlcYDqUKJk/lVMaNiw=",
        "CodeSize": 226314
    },
    "LayerArn": "arn:aws:lambda:ap-south-1:207880003428:layer:pymysql",
    "LayerVersionArn": "arn:aws:lambda:ap-south-1:207880003428:layer:pymysql:3",
    "Description": "pymysql for mysql access",
    "CreatedDate": "2021-07-15T07:15:49.564+0000",
    "Version": 3,
    "CompatibleRuntimes": [
        "python3.8"
    ]
}


[ec2-user@ip-192-168-23-47 python]$  pip install pysecret  -t .
Collecting pysecret
  Using cached pysecret-0.0.8-py2.py3-none-any.whl (57 kB)

[ec2-user@ip-192-168-23-47 python]$ cd ..
[ec2-user@ip-192-168-23-47 temp]$ ls -lt
total 8
drwxrwxr-x 4 ec2-user ec2-user   54 Jul 15 10:46 python
-rw-rw-r-- 1 ec2-user ec2-user 2915 Jul 15 10:42 mysql.py
-rw-rw-r-- 1 ec2-user ec2-user  612 Jul 15 07:06 mysql2.py
[ec2-user@ip-192-168-23-47 temp]$ zip -r9 ../pysecret.zip ./python/

[ec2-user@ip-192-168-23-47 temp]$ aws lambda publish-layer-version --layer-name pysecret --description "pysecret" --zip-file fileb://../pysecret.zip --compatible-runtimes python3.8
{
    "Content": {
        "Location": "https://awslambda-ap-s-1-layers.s3.ap-south-1.amazonaws.com/snapshots/207880003428/pysecret-10ca489e-6c8a-4870-a0de-5f4125d4c86a?versionId=nHCTKBg1JLDfpEqdANsuuARkseVeN7QV&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCmFwLXNvdXRoLTEiSDBGAiEAs8DOUtAYwaVCv6BAnnx%2FNMfv%2Bv%2F7%2FTb%2BfOYXrQbmFUwCIQD9uaMP%2F%2FizLXhodldfQGi8%2B5upOnCQ43a%2BKzkBga4KkCr8AwgrEAIaDDU0NTI1NTIwMTMwNyIMmWgoirCZYEpzTV5%2FKtkDm2587wS4p0wW44fzZPNm5PtVgPShtu8YBIu1Dziu0UtuNcj0H5jpBbbCosczYPjArffORW8gsyJPOwkyYnzJBcm4myh%2BV0mTPaJgCfdzVdIxD8%2BX8GRuM2%2Bts0eGQKBIzwQgb75PduxFqalUXFwG5GKShTcn2CArFosDJHWF6PmE3ztp1iJ%2FiEK05JGct0IwpF1gXE6obP2RHQVJ7a3giDayWWz%2BxsWIP1PYMpuNcTpZGYbclcXGcIGTaq3z5corWV7h6nksjnn6I0oWN7O28LgLAcmdd1d8%2B2xMh1OwtXrCGWy%2FLY9T%2BxtrJM2g76zN%2BSAAryGyabI0%2B%2Ffr0cPIES7dF5TNPuPbT6E5PyHbsJaYGlHMFe%2BnqYp3qyV%2BBFxIcxRZdQkEctwPU9rwMxGMTdykxdvHCAeGalZOobi1WYQ6cEMZHm9fWGfMq2LrMBJS0neRrOiOYMpvFBNgTT%2B4k2otiRSUmca%2BJ4Xb4QU%2BPdZqHB42UAnvJdNZL%2F60U841NNaEH%2F%2FhP8CXjItN%2B7RmcrW7AXXzMz1RHsiUm6pec84C7ywYQ4xjOo%2B%2ByDJjJu16%2B%2F4dZOLCFspsUs%2BVqy1DZ0rUgaZTXtbPlTP%2FnbT0cKzByx6MCZBChnUwmI3AhwY6pAFkHi2ZytFbJRBreNecwKI77MRI5%2FXB%2FwYK0vyng3saz%2B1CHs5bjQtWHs7RfCQtkK4wpDLdXrnpPd6Dor0iMbOZ1zRnlbfOztvFpxrE1hP%2B1lCGGrftoccJz3AD%2BHLcOIbR%2BJ7hDwuhKFNlHVKKLBe25CA9qoecweDRy9LyHK%2FgAPP3VSNNiTC1jmwkl2qY9p7O9zZ1jGdDjjA2cHKdwqqpt3ypsA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210715T104909Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIAX5456DINSMEQB4EA%2F20210715%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=8d75e465eb3f216bdcdfeb88f1dcd853637dab2b238b173ae297e03353cd906c",
        "CodeSha256": "o7kFhn3SaKzMywwNlpyGIlYPwHNQkaiPqWZSuH5LrYU=",
        "CodeSize": 76803
    },
    "LayerArn": "arn:aws:lambda:ap-south-1:207880003428:layer:pysecret",
    "LayerVersionArn": "arn:aws:lambda:ap-south-1:207880003428:layer:pysecret:1",
    "Description": "pysecret",
    "CreatedDate": "2021-07-15T10:49:12.919+0000",
    "Version": 1,
    "CompatibleRuntimes": [
        "python3.8"
    ]
}


Add two layers to lambda 


import pymysql 
import json 
import sys 
import boto3
from pysecret import AWSSecret
def lambda_handler(event, context):
     ssm = boto3.client('ssm')
     rds_host='database-2.cxvimhqpr2vi.ap-south-1.rds.amazonaws.com'
     parameter = ssm.get_parameter(Name='postgres-password', WithDecryption=True)
     password=parameter['Parameter']['Value']
     aws = AWSSecret()
     username = aws.get_secret_value(secret_id="mysql-username", key="username")

     print (username)

     name='admin'
     password='xxxxxxxx'
     db_name='rds'
     try:
         conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name)
     except Exception as e:
         print(str(e))
         print("ERROR: Unexpected error: Could not connect to MySql instance.")
         sys.exit()
     print("SUCCESS: Connection to RDS mysql instance succeeded")
     with conn.cursor() as cur:
        select_statement = 'select now(), DATE_SUB(NOW(), INTERVAL 4 DAY); '        
        cur.execute(select_statement)
        for doc in cur:
           print( doc )
                 
     return {
         "statusCode": 200,
         "body": json.dumps('Hello from Lambda with Layer!')
     } 

          
[ec2-user@ip-192-168-23-47 mysql]$ zip -r9 mysql.zip ./mysql/

          
Install a layer for lambda 


[ec2-user@ip-192-168-23-47 mysql]$ aws lambda publish-layer-version --layer-name pymysql \
>      --description "pymysql for mysql access" \
>      --zip-file fileb://./pymysql.zip \
>      --compatible-runtimes python3.8
{
    "Content": {
        "Location": "https://awslambda-ap-s-1-layers.s3.ap-south-1.amazonaws.com/snapshots/207880003428/pymysql-92bbc510-52bc-47d1-8f15-6d2c797d66bc?versionId=GqSOBagbac7a7UI5N.a4tN1JU330.CTR&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCmFwLXNvdXRoLTEiRzBFAiEA9c1iJ2HOQ%2BiEsxPzLf3fll0i72c%2BU1bPcPRdSqq%2BsT8CIHslqw82cdlMgQyFU0YRONrGyr%2FbQj%2B7bDqWthbMDQiFKvwDCCUQAhoMNTQ1MjU1MjAxMzA3Igx%2Bzbxq%2BkC2%2FZFvjYsq2QMvWC%2BM35URkiZnLm5NrNyDdtibwdiqnTnrxKM7qLWaRhbvIJP%2FI7AK5x4dOVVqr%2BhscpiKDLnzMQxx8yRTkNKC0vUXILsSVVRsLP63tuMoY1Liy4bdHURy8SicQ5Y6WE3BKvYOHDL0iV33WYdg%2BVEwGLU64%2FuAoOjRdoq%2BWsRk4I0%2FiA47z%2F5%2BDS%2BBaOubrrqCgMSaShd96U%2BmyFRP5I0UzOrKEbybGWoqM8%2BrPBRdMJq3i%2FsXGFxfsNKDllPLlClArqLow%2FKhOeZxIw%2B86%2BNF6TvChnYWj%2FQ7CUBdWOHLBn7m5b4KOMWWJinggGfP4XmIlW5RkzXjpwUBN08HaBcCwzytBwNz3ablAD7HDleMm5K39wt%2Bvj4%2Fp6tkq1aCZOBSVjdWPSIteDD02h8iFwCHR92ntEJE5QuNW6VCnetFqvjlM3u8BC4Z3g8efkwKhY%2B83sBxZEP76Dvo5dChIKpboItrYsUf881jXAd4FKbHLpneKrezXiAlwiAfINqWB6Ni2EWHQHoTIiD8axeLQunhLYruk5wJ3DikGiEgmCi0w17SOtp6%2BZphpsexYabrJdZDtEJnOq4a5jL%2BL24Zrh%2FT4%2Fc7jRLJSfDVCzxuV7xP22AgCX6bpgSK5jDig7%2BHBjqlAcJVes4WcrVvIHPFNtgsmdO%2FOA5uzLT7D6LkPMJPkzlgZxxKf39cSQh7m9mZa1SzYbg6CmJU2IDSX0r3LyoS6hFwqAt72p8mieBA45linERApPZ6E22m67%2BwkwYqc%2B6PyjEGTzX3Jwg%2BwwTGM1YDoWPflwvpAGRte2lt0wsZZROZHoGrDbpcOSBHoTqcPtQdfwnuHAILhnVbugnfJaEuL%2F%2FMLdv0WQ%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210715T055039Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIAX5456DINXJUOUXFB%2F20210715%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Signature=7b36cdcc1f7ebc0aab1aca5f3bb5bf7eacdf844c88e48358a1ffb36fdcb4486c",
        "CodeSha256": "ytvGQYVUr4cPihw1p5SqjqkhJ/dwB2hal7XRpRK8KrI=",
        "CodeSize": 104725
    },
    "LayerArn": "arn:aws:lambda:ap-south-1:207880003428:layer:pymysql",
    "LayerVersionArn": "arn:aws:lambda:ap-south-1:207880003428:layer:pymysql:1",
    "Description": "pymysql for mysql access",
    "CreatedDate": "2021-07-15T05:50:40.180+0000",
    "Version": 1,
    "CompatibleRuntimes": [
        "python3.8"
    ]
}




Using pymysql module
====================

import json
import pymysql

def lambda_handler(event, context):
    conn = pymysql.connect(host='', user='', database='', password='',cursorclass=pymysql.cursors.DictCursor)
    with conn.cursor() as cur:
        cur.execute("insert into myfriends values ('firstname1','lastname1')")
        conn.commit()
        cur.close()
        conn.close()
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('data inserted')
    }



import mysql.connector
import boto3
ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='rds-mysql', WithDecryption=True)

print (parameter)
mydb = mysql.connector.connect(
          host="database-3-instance-1.cxvimhqpr2vi.ap-south-1.rds.amazonaws.com",
          user="admin",
          passwd=parameter['Parameter']['Value'],
          database="pets"
          )
cursor = mydb.cursor( buffered=True)
cursor.execute("select * from test;")
result = cursor.fetchall()
for row in result:
    print(row)

mydb.disconnect()




import psycopg2
import boto3
import os
import sys
import tempfile
import csv
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3 = boto3.resource('s3')
client = boto3.client('s3')

#python3 -m pip install --user boto3
#[ec2-user@ip-192-168-23-47 ~]$ python3 4.py
#PRtLH9ITTwZawLLd
#[ec2-user@ip-192-168-23-47 ~]$ more 4.py
#import boto3
#ssm = boto3.client('ssm')
#parameter = ssm.get_parameter(Name='/Dev/postgres-47161/RDS_PASSWORD', WithDecryption=True)
#print(parameter['Parameter']['Value'])


def db_server_fetch(sql_query):
    try:
        # Make connection to db
        cxn = psycopg2.connect(CONNECT_DB)

        # Create a cursor to db
        cur = cxn.cursor()

        # Send sql query to request
        cur.execute(sql_query)
        records = cur.fetchall()

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

    finally:
        #closing database connection.
        if(cxn):
            cur.close()
            cxn.close()
            print("PostgreSQL connection is closed")
        return records



try:
    # Make connection to db
    cxn = psycopg2.connect(CONNECT_DB)
    
    # Create a cursor to db
    cur = cxn.cursor()
    
    # read file, copy to db
    with open('./vet.csv', 'r') as f:
        # skip first row, header row
        next(f)
        cur.copy_from(f, 'customers', sep=",")
        cxn.commit()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    
finally:
    #closing database connection.
    if(cxn):
        cur.close()
        cxn.close()
        print("PostgreSQL connection is closed")
        print("customers table populated")



def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = s3.Object(bucket_name, key)
    print (obj)
    with tempfile.TemporaryDirectory() as tmpdir:
        download_path = os.path.join(tmpdir, key)
        client.download_file(bucket_name, key, download_path)
        print("Downloaded s3 file, {}, to {}".format(key, download_path))
        #items = read_csv(download_path)
        #for item in items:
        #    print (item)
        try:
            connection = psycopg2.connect(user = "postgres",password = "Symantec123",host = "rdsproxy.proxy-ckzrjbfff4pm.us-east-1.rds.amazonaws.com",port = "5432", database = "postgres")

            cur = connection.cursor()
            with open(download_path,'r') as csvfile:
                # skip header
                #next(csvfile)
                csv_data = csv.reader(csvfile,delimiter=',')
                for row in csv_data:
                    logger.info(row)
                    cur.execute ('INSERT INTO customers(id,name) values ( %s ,  %s )',row)
        
                connection.commit()
        
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
    
        finally:
        #closing database connection.
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")
        
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        #cursor.execute("SELECT version();")
        #record = cursor.fetchone()
        #print("You are connected to - ", record,"\n")

        #    for idx,row in enumerate(csv_data):
        #        logger.info(row)
        #        try:
        #            cur.execute('INSERT INTO customers(id, name) VALUES("%s", "%s")', row)
        #        except Exception as e:
        #            logger.error(e)
        #        if idx % 100 == 0:
        #            connection.commit()
        #    connection.commit()
    





def read_csv(file):
    items = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {}
            data['ID'] = int(row['ID'])
            data['Name'] = row['Name']
            items.append(data)
    return items
