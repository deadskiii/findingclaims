import pandas as pd
import requests
import io
from datetime import datetime
from config import FIPS_URL, DATA_RAW, DATA_PROCESSED, OUTPUTS

def load_fips_crosswalk() -> pd.DataFrame:
    """
    Downloads the Census FIPS county crosswalk from the config URL and 
    returns a clean pandas DataFrame.
    
    Returns:
        pd.DataFrame: Cleaned dataframe with columns:
                      state_fips, county_fips, full_fips, state_abbr, county_name
    """
    response = requests.get(FIPS_URL)
    response.raise_for_status()
    
    # Read the pipe-delimited file (using dtype=str to keep leading zeros)
    df = pd.read_csv(io.StringIO(response.text), sep='|', dtype=str)
    
    # Select and rename columns mapping to the required schema
    df = df.rename(columns={
        'STATE': 'state_fips',
        'STATEFP': 'state_fips',
        'COUNTYFP': 'county_fips',
        'STUSAB': 'state_abbr',
        'COUNTYNAME': 'county_name'
    })
    
    df['full_fips'] = df['state_fips'] + df['county_fips']
    
    columns_to_keep = ['state_fips', 'county_fips', 'full_fips', 'state_abbr', 'county_name']
    df = df[[col for col in columns_to_keep if col in df.columns]]
    
    return df

def ensure_dirs() -> None:
    """
    Creates all raw, processed, and output directories if they don't already exist.
    """
    for path in DATA_RAW.values():
        path.mkdir(parents=True, exist_ok=True)
        
    for path in DATA_PROCESSED.values():
        path.mkdir(parents=True, exist_ok=True)
        
    for path in OUTPUTS.values():
        path.mkdir(parents=True, exist_ok=True)

def log(message: str, level: str = "INFO") -> None:
    """
    A simple timestamped print logger for pipeline tracking.
    
    Args:
        message (str): The message to log.
        level (str): The logging level. Defaults to 'INFO'.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {level.upper()} - {message}")
