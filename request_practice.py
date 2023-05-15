import requests

# Send a GET request to a URL and print the response content
response = requests.get('https://pypi.org/project/requests/')
#print(response.content)


# Send a POST request with data and headers
url = 'https://https://pypi.org/project/requests/'
data = {'key1': 'value1', 'key2': 'value2'}
headers = {'Content-type': 'application/json'}
response = requests.post(url, json=data, headers=headers)

# Handle errors and exceptions
response = requests.get('https://pypi.org/project/requests/')
if response.status_code == 200:
    print('Request succeeded')
else:
    print('Request failed with status code:', response.status_code)
