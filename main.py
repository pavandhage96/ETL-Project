from etl.extract import read_csv
from etl.transform import transform_data
from etl.load import load_data

def main():
    # Extract data from CSV
    df = read_csv('employee_details.csv')
    
    # Transform the data
    transformed_df = transform_data(df)
    
    # Load the data into PostgreSQL
    load_data(transformed_df)

if __name__ == "__main__":
    main()
