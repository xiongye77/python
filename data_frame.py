Method #3: Using Dataframe.assign() method

This method will create a new dataframe with new column added to the old dataframe.

# python3 -m pip install --user pandas

import pandas as pd
   
# Define a dictionary containing Students data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Height': [5.1, 6.2, 5.1, 5.2],
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']}
   
   
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Using 'Address' as the column name and equating it to the list
df2 = df.assign(address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'])
   
# Observe the result
print (df2)

#[ec2-user@ip-192-168-23-47 ~]$ python3 5.py
#     Name  Height Qualification    address
#0     Jai     5.1           Msc      Delhi
#1  Princi     6.2            MA  Bangalore
#2  Gaurav     5.1           Msc    Chennai
#3    Anuj     5.2           Msc      Patna


import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost':[10000, 5000, 15000, 2000]})

# Create a new column 'Discounted_Price' after applying
# 10% discount on the existing 'Cost' column.

# create a new column
df['Discounted_Price'] = (0.1 * df['Cost'])

# Print the DataFrame after
# addition of new column
print(df)

#[ec2-user@ip-192-168-23-47 ~]$ python3 6.py
#        Date    Event   Cost  Discounted_Price
#0  10/2/2011    Music  10000            1000.0
#1  11/2/2011   Poetry   5000             500.0
#2  12/2/2011  Theatre  15000            1500.0
#3  13/2/2011   Comedy   2000             200.0



[root@ip-192-168-23-47 ~]# pip install mysql-connector-python
Collecting mysql-connector-python
  Downloading mysql_connector_python-8.0.25-cp38-cp38-manylinux1_x86_64.whl (25.4 MB)
     |████████████████████████████████| 25.4 MB 83.4 MB/s
Collecting protobuf>=3.0.0
  Downloading protobuf-3.17.0-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)
     |████████████████████████████████| 1.0 MB 43.9 MB/s
Requirement already satisfied: six>=1.9 in /usr/local/lib/python3.8/site-packages (from protobuf>=3.0.0->mysql-connector-python) (1.15.0)
Installing collected packages: protobuf, mysql-connector-python
Successfully installed mysql-connector-python-8.0.25 protobuf-3.17.0
[root@ip-192-168-23-47 ~]# exit
logout
[ec2-user@ip-192-168-23-47 ~]$ python3 8.py

import mysql.connector




import pandas as pd

stock_df = pd.read_csv('dow_jones_index.data')
                       
stock_df.head()


ge_df = stock_df[stock_df.stock=='GE']
ibm_df = stock_df[stock_df.stock=='IBM']
krft_df = stock_df[stock_df.stock=='KRFT']

with pd.ExcelWriter('stocks.xlsx') as writer:  
    ge_df.to_excel(writer, sheet_name='GE')
    ibm_df.to_excel(writer, sheet_name='IBM')
    krft_df.to_excel(writer, sheet_name='KRFT')
      
      
my_stock_df = pd.read_excel('stocks.xlsx', sheet_name=None)  

my_stock_df.keys()
#dict_keys(['GE', 'IBM', 'KRFT'])


print (my_stock_df['GE'])

