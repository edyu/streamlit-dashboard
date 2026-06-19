import pandas as pd
import streamlit as st
from pathlib import Path
from google.cloud import bigquery, bigquery_storage

DATASET = 'sia_ceo_dashboard'
TABLE = "sales_data"

def load_data():
    service_account_info = st.secrets["bigquery"]
    client = bigquery.Client.from_service_account_info(service_account_info)
    creds = client._credentials
    storage_client = bigquery_storage.BigQueryReadClient(credentials=creds)
    project_id = service_account_info["project_id"]
    query = f"SELECT * from `{project_id}.{DATASET}.{TABLE}`"
    query_job = client.query(query)
    result = query_job.result()
    return result.to_dataframe(bqstorage_client=storage_client)

# BASE_DIR = Path(__file__).resolve().parent
# SALES_DATA_PATH = BASE_DIR / "sales_data.csv"

# def load_data():
#     return pd.read_csv(SALES_DATA_PATH)
