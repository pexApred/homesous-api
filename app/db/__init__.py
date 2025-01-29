import psycopg2
from dotenv import load_dotenv
import os

# Load the env variables from .env file
load_dotenv()

# Access the env variables
dbname=os.getenv('DB_NAME')
user=os.getenv('DB_USER')
password=os.getenv('DB_PW')
host=os.getenv('DB_HOST')
port=os.getenv('DB_PORT')

# New Database class that will be used to interact with the database

# Connect to the database with method that returns a connection object
conn = psycopg2.connect(
    dbname=dbname, 
    user=user, 
    password=password, 
    host=host, 
    port=port
)

# Create a cursor object using the cursor() method : Default = Client Side Cursors
with conn:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM users;')
    
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM freezer;')
    
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM pantry;')

    with conn.cursor() as curs:
        curs.execute('SELECT * FROM refrigerator;')
    
    # Fetch all the results from the cursor object as a list of tuples
    results = curs.fetchall()

    print(results)

# Close the cursor and the connection to the database
curs.close()
conn.close()