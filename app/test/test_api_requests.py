import unittest
from app.modules.api_requests import get_all_contries
from app.modules.error_messages import error_messages


class TestApiRequests(unittest.TestCase):

    # Successful testing, expected result type dict

    def test_valid_url(self):
        result = get_all_contries('https://restcountries.com/v3.1/all')
        self.assertTrue(result, type is dict)

    # Expected failures

    def test_connection_timeout(self):
        result = get_all_contries('http://test')
        self.assertEqual(result, error_messages('MSG_CONNECTION_ERROR'))

    def test_string_without_url(self):
        result = get_all_contries('restcountries.com/v3.1/all')
        self.assertEqual(result, error_messages('MSG_MISSING_SCHEMA'))

    def test_int(self):
        result = get_all_contries(10)
        self.assertEqual(result, error_messages('MSG_MISSING_SCHEMA'))

    def test_boolean(self):
        result = get_all_contries(0.54)
        self.assertEqual(result, error_messages('MSG_MISSING_SCHEMA'))

    def test_list(self):
        result = get_all_contries([10, 5.2, '2', True])
        self.assertEqual(result, error_messages('MSG_INVALID_URL'))

    def test_dict(self):
        result = get_all_contries({'data': 2, 'name': 'test'})
        self.assertEqual(result, error_messages('MSG_INVALID_SCHEMA'))


if __name__ == '__main__':
    unittest.main()
