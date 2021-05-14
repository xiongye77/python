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
