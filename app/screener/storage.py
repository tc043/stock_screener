import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()  # Only needed locally

SUPABASE_DB_URL = os.getenv("SUPABASE_DB_URL")
engine = create_engine(SUPABASE_DB_URL, echo=False)

def save_to_db(df, table_name="stocks_filtered"):
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)

def load_from_db(table_name="stocks_filtered"):
    return pd.read_sql(table_name, con=engine)
