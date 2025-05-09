import psycopg2
from dotenv import load_dotenv
import os

from psycopg2.extras import RealDictCursor

# Load the env variables from .env file
load_dotenv()

DB_PORT = os.getenv('DB_PORT')
DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('DB_PW')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')


# New Database class that will be used to interact with the database
class Database:
    def __init__(self):
        # Access the env variables
        self.dbname = DB_NAME
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.host = DB_HOST
        self.port = DB_PORT

        # Initialize the connection and cursor objects to None : Prevent unnecessary connections to the database
        self.conn = None
        self.curs = None

    def connect(self):
        # Connect to the database with method that returns a connection object. Try block to handle exceptions (errors)
        if self.conn is None or self.conn.closed:
            try:
                self.conn = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port
                )
                print(f"Connected to the database {DB_NAME}!")
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
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                rows = cur.fetchall()
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            rows = []
        return rows

    def query_for_first(self, query, params=None):
        results = self.query(query, params)
        return results[0] if results else None

    def execute(self, query, params=None):
        try:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()


def init_db():
    return Database()
