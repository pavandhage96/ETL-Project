import unittest
import pandas as pd
from etl.transform import transform_data

class TestTransform(unittest.TestCase):
    def test_transform_data(self):
        data = {
            'EmployeeID': [1, 2],
            'FirstName': [' John', 'Jane '],
            'LastName': ['Doe ', ' Smith'],
            'BirthDate': ['1980-01-01', '1985-02-02'],
            'Department': ['HR', 'Finance'],
            'Salary': [50000, 60000]
        }
        df = pd.DataFrame(data)
        transformed_df = transform_data(df)

        self.assertIn('FullName', transformed_df.columns)
        self.assertIn('Age', transformed_df.columns)
        self.assertIn('SalaryBucket', transformed_df.columns)
        self.assertNotIn('FirstName', transformed_df.columns)
        self.assertNotIn('LastName', transformed_df.columns)
        self.assertNotIn('BirthDate', transformed_df.columns)
        self.assertEqual(transformed_df.loc[0, 'FullName'], 'John Doe')
        self.assertEqual(transformed_df.loc[1, 'FullName'], 'Jane Smith')

if __name__ == '__main__':
    unittest.main()
