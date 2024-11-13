import unittest
from etl.extract import read_csv

class TestExtract(unittest.TestCase):
    def test_read_csv(self):
        df = read_csv('employee_details__1_-1.csv')
        self.assertIsNotNone(df)
        self.assertIn('EmployeeID', df.columns)
        self.assertIn('FirstName', df.columns)
        self.assertIn('LastName', df.columns)

if __name__ == '__main__':
    unittest.main()
