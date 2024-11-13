import pandas as pd

def read_csv(/FileStore/tables/employee_details__1_-1.csv):

    try:
        df = pd.read_csv(/FileStore/tables/employee_details__1_-1.csv)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
