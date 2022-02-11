from libs.api_requests import get_all_contries


def run():
    print('Initiating execution...')
    print('Obtaining information from countries...')
    info_countries = get_all_contries()
    print(info_countries)


if __name__ == '__main__':
    run()
