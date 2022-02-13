import requests
from app.modules.error_messages import error_messages


def get_all_contries(url):

    # Requests: HTTP for Humans
    # Documentation:  https://docs.python-requests.org/en/latest/

    # The information is obtained from the countries and returned without any processing.
    try:
        print('Obtaining information from countries... 🌎')
        r = requests.get(url)
        return(r.json())
    except requests.exceptions.MissingSchema:
        return error_messages('MSG_MISSING_SCHEMA')
    except requests.exceptions.InvalidURL:
        return error_messages('MSG_INVALID_URL')
    except requests.exceptions.InvalidSchema:
        return error_messages('MSG_INVALID_SCHEMA')
    except requests.exceptions.ConnectionError:
        return error_messages('MSG_CONNECTION_ERROR')
