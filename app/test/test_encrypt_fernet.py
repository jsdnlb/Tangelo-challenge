import unittest
from app.modules.encrypt_fernet import encrypt_fernet
from app.modules.error_messages import error_messages


class TestEncryptSHA1(unittest.TestCase):

    # Successful testing, expected result bites

    def test_string(self):
        result = encrypt_fernet('test')
        self.assertTrue(result, type is bytes)


    # Expected failures

    def test_int(self):
        result = encrypt_fernet(10)
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))

    def test_boolean(self):
        result = encrypt_fernet(0.54)
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))

    def test_list(self):
        result = encrypt_fernet([10, 5.2, '2', True])
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))

    def test_dict(self):
        result = encrypt_fernet({'data': 2, 'name': 'test'})
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))


if __name__ == '__main__':
    unittest.main()
