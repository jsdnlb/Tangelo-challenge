import requests


def get_all_contries(url):

    # Requests: HTTP for Humans
    # Documentation:  https://docs.python-requests.org/en/latest/

    # The information is obtained from the countries and returned without any processing.
    try:
        print('Obtaining information from countries... 🌎')
        r = requests.get(url)
        return(r.json())
    except requests.exceptions.MissingSchema:
        return 'Invalid URL. No schematic has been provided. Try adding http://'
    except requests.exceptions.InvalidURL:
        return 'Failed to parse. Enter a valid URL. Try adding http://'
    except requests.exceptions.InvalidSchema:
        return 'No connection adapters were found. Enter a valid URL. Try adding http://'
    except requests.exceptions.ConnectionError:
        return 'Failed to establish a new connection: Connection timed out'
