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

        # Initialize the connection and cursor objects to None : Prevent unnecessary connections to the database
        self.conn = None
        self.curs = None
    
    def connect(self):
        # Connect to the database with method that returns a connection object. Try block to handle exceptions (errors)
        try: 
            self.conn = psycopg2.connect(
                dbname=self.dbname, 
                user=self.user, 
                password=self.password, 
                host=self.host, 
                port=self.port
            )
            print("Connected to the database!")
        # Handle any exceptions that occur during the connection process
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    # Close() method explicitly closes the cursor and connection objects | Proper cleanup to prevent memory leaks | 
    # SIDENOTE: __del__ method is a finalizer that is called by the garbage collector when an object is deleted or about to be destroyed

    def close(self):
        if self.curs:
            self.curs.close()
        
        if self.conn:
            self.conn.close()
            print("Connection to the database is closed!")

    # Query method without the need to return any results : INSERT, UPDATE, DELETE : No unnecessary fetches of results
    def query(self, query, params=None):
        try:
            with self.conn.cursor() as cur:
                cur.execute(query, params)
                rows = cur.fetchall() if cur.description else None
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            rows = None
        return rows