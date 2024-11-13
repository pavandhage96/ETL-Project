import os
import pandas as pd
import psycopg2
from psycopg2 import sql

def load_data(df):
    
    try:
        
        host = os.getenv('POSTGRES_HOST', 'localhost')
        port = os.getenv('POSTGRES_PORT', 5432)
        dbname = os.getenv('POSTGRES_DB', 'employee_db')
        user = os.getenv('POSTGRES_USER', 'postgres')
        password = os.getenv('POSTGRES_PASSWORD', '1234')

        # Establish a connection to PostgreSQL
        conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
        cursor = conn.cursor()

        # Create table if not exists
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS employee (
            EmployeeID INT PRIMARY KEY,
            FullName VARCHAR(100),
            Department VARCHAR(50),
            Salary INT,
            Age INT,
            SalaryBucket CHAR(1)
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()

        # Insert data into the table
        for _, row in df.iterrows():
            insert_query = sql.SQL('''
            INSERT INTO employee (EmployeeID, FullName, Department, Salary, Age, SalaryBucket)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (EmployeeID) DO NOTHING;
            ''')
            cursor.execute(insert_query, tuple(row))
        conn.commit()

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

    return None
