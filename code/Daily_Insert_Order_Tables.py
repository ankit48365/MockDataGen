import pyodbc
import random
from datetime import datetime, timedelta
import os

# Establish a connection to your database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=localhost;'
                      'DATABASE=POC;'
                      'UID=poc_login;'
                      'PWD=Dominos#2023')

cursor = conn.cursor()

# Get the maximum order_id
cursor.execute("SELECT MAX([order_id]) AS MaxOrderID FROM [POC].[pizza].[orders]")
Max_OrID = cursor.fetchone()[0]

print('max order id is' , Max_OrID)

# Get the maximum order_details_id
cursor.execute("SELECT MAX([order_details_id]) AS MaxOrderDetID FROM [POC].[pizza].[order_details]")
Max_detid = cursor.fetchone()[0]
print('max order  detail id is' , Max_detid)
# NewOrderDetID = Max_detid + 1

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

#this tuple will help determine was new orderid's were generated in that run
order_id_tuple = ()

# hardcoded pizza_id tuple
pizza_id = ('bbq_ckn_l', 'bbq_ckn_m', 'bbq_ckn_s', 'big_meat_s', 'calabrese_m')

# Random Pizza Quantity
RandQ = [1,2,3,4]


# Generate 3 new records in order table
for i in range(1, 4):
    # Generate a random time between 8:00:00 and 16:00:00
    random_time = (datetime.now().replace(hour=8, minute=0, second=0) + timedelta(seconds=random.randint(0, 8*3600))).time()
    
    # Create the new order_id
    new_order_id = Max_OrID + i

    # Add the new order_id to the tuple
    order_id_tuple+= (new_order_id,)

    # Create the insert query
    query = f"INSERT INTO [POC].[pizza].[orders] ([order_id],[date],[time]) VALUES('{new_order_id}','{current_date}', '{random_time}')"
    print(query)
    # Execute the query
    cursor.execute(query)

# Generate 3 new records in order detail table
# for i in range(1, 4):
for i in order_id_tuple:


    # Create the new order_detail_id
    # new_order_det_id = NewOrderDetID + 1
    Max_detid = Max_detid + 1


    rand_num = random.choice(RandQ)
    random_pizza_id = random.choice(pizza_id)

    # Create the insert query
    query1 = f"INSERT INTO [POC].[pizza].[order_details] ([order_details_id] ,[order_id] ,[pizza_id] ,[quantity]) VALUES('{Max_detid}','{i}', '{random_pizza_id}','{rand_num}')"
    print(query1)
    # Execute the query
    cursor.execute(query1)

# print (order_id_tuple)

# Commit the changes
conn.commit()

# Close the connection
conn.close()






# # Get the environment variables
# driver = os.environ['DB_DRIVER']
# # server = os.environ['DB_SERVER']
# database = os.environ['DB_DATABASE']
# uid = os.environ['DB_UID']
# pwd = os.environ['DB_PWD']

# conn = pyodbc.connect(f'DRIVER={{{driver}}};'
#                       f'SERVER=localhost;'
#                       f'DATABASE={database};'
#                       f'UID={uid};'
#                       f'PWD={pwd}')

