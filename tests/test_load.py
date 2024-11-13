import unittest
import pandas as pd
from unittest.mock import patch
from etl.load import load_data

class TestLoad(unittest.TestCase):
    @patch('etl.load.psycopg2.connect')
    def test_load_data(self, mock_connect):
        data = {
            'EmployeeID': [1, 2],
            'FullName': ['John Doe', 'Jane Smith'],
            'Department': ['HR', 'Finance'],
            'Salary': [50000, 60000],
            'Age': [43, 38],
            'SalaryBucket': ['B', 'B']
        }
        df = pd.DataFrame(data)
        load_data(df)
        self.assertTrue(mock_connect.called)

if __name__ == '__main__':
    unittest.main()
