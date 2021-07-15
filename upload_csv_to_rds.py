[ec2-user@ip-192-168-23-47 mysql]$ python3 -m pip install -t . PyMySQL
Collecting PyMySQL
  Using cached PyMySQL-1.0.2-py3-none-any.whl (43 kB)
Installing collected packages: PyMySQL
Successfully installed PyMySQL-1.0.2
[ec2-user@ip-192-168-23-47 mysql]$ ls -lt
total 0
drwxrwxr-x 2 ec2-user ec2-user 119 Jul 15 02:17 PyMySQL-1.0.2.dist-info
drwxrwxr-x 4 ec2-user ec2-user 226 Jul 15 02:17 pymysql
[ec2-user@ip-192-168-23-47 mysql]$ cd pymysql/
[ec2-user@ip-192-168-23-47 pymysql]$ ls -l
total 132
-rw-rw-r-- 1 ec2-user ec2-user  7399 Jul 15 02:17 _auth.py
-rw-rw-r-- 1 ec2-user ec2-user 10293 Jul 15 02:17 charset.py
-rw-rw-r-- 1 ec2-user ec2-user 51251 Jul 15 02:17 connections.py
drwxrwxr-x 3 ec2-user ec2-user   165 Jul 15 02:17 constants
-rw-rw-r-- 1 ec2-user ec2-user  9430 Jul 15 02:17 converters.py
-rw-rw-r-- 1 ec2-user ec2-user 15366 Jul 15 02:17 cursors.py
-rw-rw-r-- 1 ec2-user ec2-user  3773 Jul 15 02:17 err.py
-rw-rw-r-- 1 ec2-user ec2-user  4391 Jul 15 02:17 __init__.py
-rw-rw-r-- 1 ec2-user ec2-user   573 Jul 15 02:17 optionfile.py
-rw-rw-r-- 1 ec2-user ec2-user 11859 Jul 15 02:17 protocol.py
drwxrwxr-x 2 ec2-user ec2-user   310 Jul 15 02:17 __pycache__
-rw-rw-r-- 1 ec2-user ec2-user   360 Jul 15 02:17 times.py

          
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
