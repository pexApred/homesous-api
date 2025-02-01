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
            # Create a cursor object using the cursor() method : Default = Client Side Cursors
            self.curs = self.conn.cursor()
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

    # Dunder methods __enter__ and _-exit__ to allow the Database class to be used as a context manager(with statement) : Explicit calls to connect() and close() methods are not needed : Automatically called when the with statement is used
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception happened: {exc_val}")
        self.close()

    # Query method without the need to return any results : INSERT, UPDATE, DELETE : No unnecessary fetches of results
    def query(self, query, params=None):
        try:
            # Runs the SQL query
            self.curs.execute(query, params)
            # Ensures changes (INSERT, UPDATE, DELETE) are committed to the database
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")

    # Query to fetch results from the database : SELECT : Explicitly fetch the results
    def fetch_query_results(self):            
        # Fetch all the results from the cursor object as a list of tuples 
        results = self.curs.fetchall()
        return results if self.curs else None
    # Can modulize further by having control over how many rows to retrieve : "def fetch_one(self):" or "def fetch_many(self, size):"

# Test the Database class & Check Connection to postgres: default database prior to creating own database
if __name__ == "__main__":
    try: 
        with Database() as db:
            db.query("SELECT 1;")  # Simple query to check connection
            result = db.curs.fetchone()
            print(f"WORKING?: {result}")
    except Exception as e:
        print(f"Database connection failed: {e}")