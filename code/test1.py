import pyodbc
import random
from datetime import datetime, timedelta

# Establish a connection to your database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=localhost;'
                      'DATABASE=POC;'
                      'UID=poc_login;'
                      'PWD=Dominos#2023')



cursor = conn.cursor()

# Get the maximum order_id
cursor.execute("SELECT MAX([order_id]) AS MaxOrderID FROM [POC].[pizza].[orders]")
max_id = cursor.fetchone()[0]

# Get the maximum order_details_id
cursor.execute("SELECT MAX([order_details_id]) AS MaxOrderDetID FROM [POC].[pizza].[order_details]")
max_det_id = cursor.fetchone()[0]


# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

#this tuple will help determine was new orderid's were generated in that run
order_id_tuple = ()

# Generate 3 new records
for i in range(1, 4):
    # Generate a random time between 8:00:00 and 16:00:00
    random_time = (datetime.now().replace(hour=8, minute=0, second=0) + timedelta(seconds=random.randint(0, 8*3600))).time()
    
    # Create the new order_id
    new_order_id = max_id + i

    # Add the new order_id to the tuple
    order_id_tuple+= (new_order_id,)

    # Create the insert query
    # query = f"INSERT INTO [POC].[pizza].[orders] ([order_id],[date],[time]) VALUES('{new_order_id}','{current_date}', '{random_time}')"
    
    # Execute the query
    # cursor.execute(query)

    

print (order_id_tuple)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
