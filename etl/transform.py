import pandas as pd
from datetime import datetime

def transform_data(df):
    """Transform the data according to specified business rules."""
    if df is None:
        return None

    # Date Format Conversion
    df['BirthDate'] = pd.to_datetime(df['BirthDate']).dt.strftime('%d/%m/%Y')

    # Data Cleaning
    df['FirstName'] = df['FirstName'].str.strip()
    df['LastName'] = df['LastName'].str.strip()

    # Full Name Creation
    df['FullName'] = df['FirstName'] + ' ' + df['LastName']

    # Age Calculation
    df['Age'] = df['BirthDate'].apply(lambda x: 2023 - int(x.split('/')[-1]))

    # Salary Categorization
    df['SalaryBucket'] = df['Salary'].apply(lambda x: 'A' if x < 50000 else 'B' if x <= 100000 else 'C')

    # Column Removal
    df.drop(columns=['FirstName', 'LastName', 'BirthDate'], inplace=True)

    return df
