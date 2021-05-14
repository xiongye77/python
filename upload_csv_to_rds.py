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
