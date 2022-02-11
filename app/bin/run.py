from time import sleep
from app.libs.api_requests import get_all_contries
from app.libs.structure_dataframe import filter_data
from app.libs.calculating_run_times import calculate_execution_times


def run():
    print('Initiating execution...')
    print('Obtaining information from countries...')
    info_countries = get_all_contries("https://restcountries.com/v3.1/all")
    print('Filtering the required data...\n')
    sleep(2)
    data = filter_data(info_countries)
    print(data)
    sleep(2)
    print('\nCalculating table execution times...\n')
    all_table_execution_times = calculate_execution_times(data)
    print('Minimum time: ', str(all_table_execution_times['min_time']) + ' ms')
    print('Maximum time: ', str(all_table_execution_times['max_time']) + ' ms')
    print('Average time: ', str(all_table_execution_times['average_time']) + ' ms')
    print('Total time: ', str(all_table_execution_times['total_time']) + ' ms\n')
    print('Saving the information in the database...\n')



if __name__ == '__main__':
    run()
