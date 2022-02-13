import unittest
from app.modules.connect_and_insert_in_table import connect_and_insert_log
from app.modules.error_messages import error_messages


class TestConnectAndInsertSQLite(unittest.TestCase):

    # Successful testing, expected result True

    def test_tuple(self):
        result = connect_and_insert_log((0.82, 0.03, 0.5, 10))
        self.assertTrue(result)

    # Expected failures

    def test_tuple_incomplete(self):
        result = connect_and_insert_log((0.82, 0.03,))
        self.assertEqual(result, error_messages('MSG_SQLITE_ERROR'))

    def test_string(self):
        result = connect_and_insert_log('testing')
        self.assertEqual(result, error_messages('MSG_SQLITE_ERROR'))

    def test_int(self):
        result = connect_and_insert_log(2)
        self.assertEqual(result, error_messages('MSG_SQLITE_VALUE_ERROR'))

    def test_boolean(self):
        result = connect_and_insert_log(2.4)
        self.assertEqual(result, error_messages('MSG_SQLITE_VALUE_ERROR'))

    def test_empty(self):
        result = connect_and_insert_log('')
        self.assertEqual(result, error_messages('MSG_SQLITE_ERROR'))

    def test_dict(self):
        result = connect_and_insert_log({'test': 'test', 'time': 1})
        print('####', result)
        self.assertEqual(result, error_messages('MSG_SQLITE_ERROR'))


if __name__ == '__main__':
    unittest.main()
