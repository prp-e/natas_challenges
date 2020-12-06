import requests

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = "http://natas15.natas.lab.overthewire.org/"

session = requests.Session()
response = session.post(url, auth=(username, password))

print(response.text)
