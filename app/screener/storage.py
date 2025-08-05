import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables
load_dotenv()

# Fetch variables
SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

# Verify environment variables
print("DB URL:", SUPABASE_DB_URL)
print("Credentials:", USER, PASSWORD, HOST, PORT, DBNAME)

# SQLAlchemy/pandas functions
engine = create_engine(SUPABASE_DB_URL, echo=True)  # Enable echo for debugging

def save_to_db(df, table_name="stocks_filtered"):
    try:
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f"Data saved to table {table_name}")
    except Exception as e:
        print(f"Failed to save data: {e}")

def load_from_db(table_name="stocks_filtered"):
    try:
        df = pd.read_sql(table_name, con=engine)
        print(f"Data loaded from table {table_name}")
        return df
    except Exception as e:
        print(f"Failed to load data: {e}")
        return None

# Test psycopg2 connection
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME,
    )
    print("Connection successful!")
    
    cursor = connection.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
