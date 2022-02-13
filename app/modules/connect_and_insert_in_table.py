from app.modules.error_messages import error_messages
import sqlite3
import pandas as pd


MSG_SQLITE_ERROR = 'Validate the structure of the data, expected tuple, example (0.82,0.03,0.5,10)'
MSG_VALUE_ERROR = 'Invalid parameters expected tuple, example (0.82,0.03,0.5,10)'


def connect_and_insert_log(data_time):
    try:
        print('Saving information in the database... 💾\n')

        # Documentation: https://pynative.com/python-sqlite/
        # Database created and connect
        sqliteConnection = sqlite3.connect('SQLite_test.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        # Create the table log_execution_time if it does not exist
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS log_execution_time (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    max_time REAL NOT NULL,
                    min_time REAL NOT NULL,
                    average_time REAL NOT NULL,
                    total_time REAL NOT NULL,
                    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                );""")
        print('Create new register.')

        # Data is inserted into the table
        cursor.execute("INSERT INTO log_execution_time( max_time, min_time, average_time, total_time) VALUES(?,?,?,?);", data_time)
        sqliteConnection.commit()

        # Saving the table log_execution_time in a json taking advantage of DataFram's features
        db_df = pd.read_sql_query("SELECT * FROM log_execution_time", sqliteConnection)
        print('Saving the table log_execution_time in a json.')
        db_df.to_json('log_execution_time.json')

        return True
        
    except sqlite3.Error:
        return error_messages('MSG_SQLITE_ERROR')
    except ValueError:
        return error_messages('MSG_SQLITE_VALUE_ERROR')
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed.")