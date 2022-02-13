# Write all the error messages and then return the answer.

def error_messages(msg):
    messages = {
        # Errors api_request
        'MSG_MISSING_SCHEMA': 'Invalid URL. No schema has been provided. Try adding http://',
        'MSG_INVALID_URL': 'Failed to parse. Enter a valid URL. Try adding http://',
        'MSG_INVALID_SCHEMA': 'No connection adapters were found. Enter a valid URL. Try adding http://',
        'MSG_CONNECTION_ERROR': 'Failed to establish a new connection: Connection timed out',
        # Error structure_dataframe
        'MSG_INVALID_PARAMETERS': 'Invalid parameters, validate the information entered.',
        # Errors connect_and_insert_sqlite
        'MSG_SQLITE_ERROR': 'Validate the structure of the data, expected tuple, example (0.82,0.03,0.5,10)',
        'MSG_SQLITE_VALUE_ERROR': 'Invalid parameters expected tuple, example (0.82,0.03,0.5,10)',
        # Error encrypt_sha1
        'MSG_TYPE_ERROR': 'Invalid parameters, enter a string',
        # Errors calculate_run_times
        'MSG_RUNTIMES_TYPE_ERROR': 'Invalid parameters, validate the information entered.',
        'MSG_RUNTIMES_KEY_ERROR': 'Invalid parameters, must send a DataFrame'
    }

    return messages[msg]
