from libs.api_requests import get_all_contries
from libs.structure_dataframe import filter_data


def run():
    print('Initiating execution...')
    print('Obtaining information from countries...')
    info_countries = get_all_contries()
    print('Filtering the required data...')
    data = filter_data(info_countries)
    print(data)


if __name__ == '__main__':
    run()
