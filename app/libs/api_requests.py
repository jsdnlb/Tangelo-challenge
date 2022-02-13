import requests


MSG_MISSING_SCHEMA = 'Invalid URL. No schematic has been provided. Try adding http://'
MSG_INVALID_URL = 'Failed to parse. Enter a valid URL. Try adding http://'
MSG_INVALID_SCHEMA = 'No connection adapters were found. Enter a valid URL. Try adding http://'
MSG_CONNECTION_ERROR = 'Failed to establish a new connection: Connection timed out'


def get_all_contries(url):

    # Requests: HTTP for Humans
    # Documentation:  https://docs.python-requests.org/en/latest/

    # The information is obtained from the countries and returned without any processing.
    try:
        print('Obtaining information from countries... 🌎')
        r = requests.get(url)
        return(r.json())
    except requests.exceptions.MissingSchema:
        return MSG_MISSING_SCHEMA
    except requests.exceptions.InvalidURL:
        return MSG_INVALID_URL
    except requests.exceptions.InvalidSchema:
        return MSG_INVALID_SCHEMA
    except requests.exceptions.ConnectionError:
        return MSG_CONNECTION_ERROR
