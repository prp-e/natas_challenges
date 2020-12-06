import requests

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://natas16.natas.labs.overthewire.org/' 

session = requests.Session()
response = session.post(url, auth=(username, password))

print(response.text)
