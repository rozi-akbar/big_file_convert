import json
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="rozi_convert"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# initialize product_list
productsList = []

# load big json
with open('../Data2.json') as p:
    for jsonObj in p:
        productsList.append(json.loads(jsonObj))
        print(productsList)

# insert data to database
# print("Inserting each JSON Decoded Object")
# for product in productsList:
    # cur.execute("INSERT INTO products (_id, Code, SKU, BatchNumber, Hash, SortenUrl, UploadId, IsActivated, CreatedDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (product['_id']['$numberLong'], product['Code'], product['SKU'], product['BatchNumber'], product['Hash'], product['SortenUrl'], product['UploadId'], product['IsActived'], product['CreatedDate']['$date']))
    # print(product['_id']['$numberLong'],"/",product['Code'],"/",product['SKU'],"/",product['BatchNumber'],"/",product['Hash'],"/",product['SortenUrl'],"/",product['UploadId'],"/",product['IsActived'],"/",product['CreatedDate']['$date'])
    # try: 
        # cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))
        # print(product['_id']['$numberLong'],"/",product['Code'],"/",product['SKU'],"/",product['BatchNumber'],"/",product['Hash'],"/",product['SortenUrl'],"/",product['UploadId'],"/",product['IsActived'],"/",product['CreatedDate']['$date'])
        # cur.execute("INSERT INTO rozi_convert.products (_id, Code, SKU, BatchNumber, Hash, SortenUrl, UploadId, IsActivated, CreatedDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (product['_id']['$numberLong'], product['Code'], product['SKU'], product['BatchNumber'], product['Hash'], product['SortenUrl'], product['UploadId'], product['IsActived'], product['CreatedDate']['$date']))
        # conn.commit()
        # cur.execute("SELECT _id, Code FROM products")
        # for _id, Code in cur: 
        #     print(f"First name: {_id}, Last name: {Code}")
    # except mariadb.Error as e: 
    #     print(f"Error: {e}")

# print("Success")