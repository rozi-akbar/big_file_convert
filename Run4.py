# Import Package
import mariadb
import sys
import jsonlines

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

with jsonlines.open('../Data.json') as reader:
    for product in reader:
        try: 
            # cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))
            # print(product['_id']['$numberLong'],"/",product['Code'],"/",product['SKU'],"/",product['BatchNumber'],"/",product['Hash'],"/",product['SortenUrl'],"/",product['UploadId'],"/",product['IsActived'],"/",product['CreatedDate']['$date'])
            cur.execute("INSERT INTO rozi_convert.products (_id, Code, SKU, BatchNumber, Hash, SortenUrl, UploadId, IsActivated, CreatedDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (product['_id']['$numberLong'], product['Code'], product['SKU'], product['BatchNumber'], product['Hash'], product['SortenUrl'], product['UploadId'], product['IsActived'], product['CreatedDate']['$date']))
            conn.commit()
            # cur.execute("SELECT _id, Code FROM products")
            # for _id, Code in cur: 
            # print(f"First name: {_id}, Last name: {Code}")
        except mariadb.Error as e: 
            print(f"Error: {e}")