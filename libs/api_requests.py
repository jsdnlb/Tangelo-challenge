import requests


def get_all_contries():

    # Requests: HTTP for Humans
    # Documentation:  https://docs.python-requests.org/en/latest/

    # The information is obtained from the countries and returned without any processing.
    url = "https://restcountries.com/v3.1/all"
    r = requests.get(url)
    return(r.json())


if __name__ == '__main__':
    get_all_contries()
