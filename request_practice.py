import requests

# Send a GET request to a URL and print the response content
# response = requests.get('https://www.investopedia.com')
# print(response.content)

import requests 
import json

url = ("api.example.com/v1.11/user?id=123456")
header = {"Authorization": "hibnn:11111:77788777YT666:CAL1"} 
response = requests.get(url, headers=header) 
print(response.json)

# # Send a POST request with data and headers
# url = 'https://www.investopedia.com'
# data = {'key1': 'value1', 'key2': 'value2'}
# headers = {'Content-type': 'application/json'}
# response = requests.post(url, json=data, headers=headers)

# # Handle errors and exceptions
# response = requests.get('https://www.investopedia.com')
# if response.status_code == 200:
#     print('Request succeeded')
# else:
#     print('Request failed with status code:', response.status_code)
