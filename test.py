import sys
import math
import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

if __name__ == '__main__':
    print('test')
    num = sys.argv[1].split(",")
    print(num)