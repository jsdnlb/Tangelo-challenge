from time import sleep
from app.libs.api_requests import get_all_contries
from app.libs.connect_and_insert_in_table import connect_and_insert_log
from app.libs.structure_dataframe import filter_data
from app.libs.calculating_run_times import calculate_execution_times


def run():
    print('Initiating execution... 🚀')
    info_countries = get_all_contries("https://restcountries.com/v3.1/all")
    sleep(2)
    data = filter_data(info_countries)
    # I use the tuple returned by calculate_execution_times() to send them to the database.
    all_times = calculate_execution_times(data)
    sleep(2)
    connect_and_insert_log(all_times)
    sleep(2)
    print('\nEverything was executed correctly, thank you for testing it 🥳!\n')


if __name__ == '__main__':
    run()
