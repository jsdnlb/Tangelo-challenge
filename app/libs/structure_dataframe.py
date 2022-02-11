import pandas as pd
from timeit import default_timer as timer
from app.libs.encrypt_sha1 import encrypt_sha1


def filter_data(data):

    region = []
    country_name = []
    language = []
    execution_time = []

    for elem in data:
        # Calculation in initial execution time
        start_time = timer()
        region.append(elem['region'])
        country_name.append(elem['name']['common'])
        # Valid if the language exists, otherwise encrypt 'Language not found'.
        try:
            # First, I capture only the values of the elem['languages'], this return a dict_values.
            # Then use [* operator] to unpack dict_values with this it becomes a list and I get the value in the index[0]
            # Finally use the function to encrypt SHA1
            # More information about unpack here: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
            language.append(encrypt_sha1([*elem['languages'].values()][0]))
        except KeyError:
            language.append(encrypt_sha1('Language not found'))
        # Calculation in final execution time
        end_time = timer()
        # I subtract the final execution time from the initial time, multiply it by 1000 to convert it to milliseconds
        # then round it to 2 digits and finally convert it to a string for display.
        execution_time.append(round((end_time - start_time)*1000, 2))

    # Generating table with DataFrame
    table = pd.DataFrame({
        "Region": region,
        "Country": country_name,
        "Language": language,
        "Time": execution_time
    })

    return table
