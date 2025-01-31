import psycopg2
from dotenv import load_dotenv
import os

# Load the env variables from .env file
load_dotenv()
# New Database class that will be used to interact with the database

class Database:
    def __init__(self):
        # Access the env variables
        self.dbname=os.getenv('DB_NAME')
        self.user=os.getenv('DB_USER')
        self.password=os.getenv('DB_PW')
        self.host=os.getenv('DB_HOST')
        self.port=os.getenv('DB_PORT')
        
    # Connect to the database with method that returns a connection object
        self.conn = psycopg2.connect(
            dbname=self.dbname, 
            user=self.user, 
            password=self.password, 
            host=self.host, 
            port=self.port
        )
        # Create a cursor object using the cursor() method : Default = Client Side Cursors
        self.curs = self.conn.cursor()

    def query(self, query):
        self.curs.execute(query)
        # Fetch all the results from the cursor object as a list of tuples
        results = self.curs.fetchall()
        return results

    def __del__(self):
        # Close the cursor and the connection to the database
        self.curs.close()
        self.conn.close()

# Access the env variables
# dbname=os.getenv('DB_NAME')
# user=os.getenv('DB_USER')
# password=os.getenv('DB_PW')
# host=os.getenv('DB_HOST')
# port=os.getenv('DB_PORT')

# conn = psycopg2.connect(
#     dbname=dbname, 
#     user=user, 
#     password=password, 
#     host=host, 
#     port=port
# )

# with conn:
#     with conn.cursor() as curs:
#         curs.execute('SELECT * FROM users;')
    
#     with conn.cursor() as curs:
#         curs.execute('SELECT * FROM freezer;')
    
#     with conn.cursor() as curs:
#         curs.execute('SELECT * FROM pantry;')

#     with conn.cursor() as curs:
#         curs.execute('SELECT * FROM refrigerator;')
    
#     results = curs.fetchall()

#     print(results)

# curs.close()
# conn.close()