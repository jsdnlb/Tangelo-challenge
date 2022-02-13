import unittest
import pandas as pd
from app.modules.calculate_run_times import calculate_execution_times
from app.modules.error_messages import error_messages


class TestRunTimes(unittest.TestCase):

    # Successful testing, expected result Tuple with values (max, min, average and tota)

    def test_data_frame(self):
        table = pd.DataFrame({
            "Time": [2, 0.2, 10, 2.2, 3, 4, 4]
        })
        result = calculate_execution_times(table)
        self.assertEqual(result, (10.0, 0.2, 3.63, 25.4))

    # Expected failures

    def test_string(self):
        result = calculate_execution_times('test')
        self.assertEqual(result, error_messages('MSG_RUNTIMES_TYPE_ERROR'))

    def test_int(self):
        result = calculate_execution_times(10)
        self.assertEqual(result, error_messages('MSG_RUNTIMES_TYPE_ERROR'))

    def test_boolean(self):
        result = calculate_execution_times(0.54)
        self.assertEqual(result, error_messages('MSG_RUNTIMES_TYPE_ERROR'))

    def test_list(self):
        result = calculate_execution_times([10, 5.2, '2', True])
        self.assertEqual(result, error_messages('MSG_RUNTIMES_TYPE_ERROR'))

    def test_dict(self):
        result = calculate_execution_times({'data': 2, 'name': 'test'})
        self.assertEqual(result, error_messages('MSG_RUNTIMES_KEY_ERROR'))


if __name__ == '__main__':
    unittest.main()
