import duckdb
import pandas as pd
from config import DB_PATH

def get_connection() -> duckdb.DuckDBPyConnection:
    """
    Establishes and returns a DuckDB connection to the project's database file.
    
    Returns:
        duckdb.DuckDBPyConnection: Connection to the main database.
    """
    return duckdb.connect(database=str(DB_PATH), read_only=False)

def create_schema() -> None:
    """
    Creates empty tables (shells) for each of the 6 data sources 
    if they do not already exist. Columns are TBD per notebook.
    """
    conn = get_connection()
    try:
        queries = [
            "CREATE TABLE IF NOT EXISTS cms_medicare (id INTEGER)",
            "CREATE TABLE IF NOT EXISTS seer_cancer (id INTEGER)",
            "CREATE TABLE IF NOT EXISTS cdc_places (id INTEGER)",
            "CREATE TABLE IF NOT EXISTS lana_directory (id INTEGER)",
            "CREATE TABLE IF NOT EXISTS advocacy_groups (id INTEGER)",
            "CREATE TABLE IF NOT EXISTS apcd_claims (id INTEGER)"
        ]
        
        for q in queries:
            conn.execute(q)
    finally:
        conn.close()

def run_query(sql: str) -> pd.DataFrame:
    """
    Executes a SQL query against the DuckDB database and returns the result as a pandas DataFrame.
    
    Args:
        sql (str): SQL query to run.
        
    Returns:
        pd.DataFrame: Query results in a dataframe format.
    """
    conn = get_connection()
    try:
        return conn.execute(sql).df()
    finally:
        conn.close()
