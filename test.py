import sys
import math
import requests
from requests.exceptions import HTTPError

def test():
    #x = requests.get('https://w3schools.com/python/demopage.htm')
    for url in ['https://api.github.com', 'https://api.github.com/invalid']:
        try:
            response = requests.get(url)

        # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')


if __name__ == '__main__':
    print('test')
    num = sys.argv[1].split(",")
    print(num)
    test()
    response = requests.head('https://httpbin.org/get')
    print(response.headers['Content-Type'])