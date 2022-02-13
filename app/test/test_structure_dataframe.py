import unittest
import json
from app.libs.structure_dataframe import filter_data

# Error messages
MSG_TYPE_ERROR = 'Invalid parameters, validate the information entered.'


class TestStructureDataFrame(unittest.TestCase):

    # Successful testing, expected result DataFrame

    """ def test_dict_allowed(self):
        with open('test_sample_countries.json', 'r') as j:
            data = json.load(j)
            print(data)
        result = filter_data(data)
        self.assertEqual(result, DATAFRAME) """


    # Expected failures

    def test_string(self):
        result = filter_data('test')
        self.assertEqual(result, MSG_TYPE_ERROR)

    def test_int(self):
        result = filter_data(10)
        self.assertEqual(result, MSG_TYPE_ERROR)

    def test_boolean(self):
        result = filter_data(0.54)
        self.assertEqual(result, MSG_TYPE_ERROR)

    def test_list(self):
        result = filter_data([10, 5.2, '2', True])
        self.assertEqual(result, MSG_TYPE_ERROR)

    def test_dict(self):
        result = filter_data({'data': 2, 'name': 'test'})
        self.assertEqual(result, MSG_TYPE_ERROR)


if __name__ == '__main__':
    unittest.main()
