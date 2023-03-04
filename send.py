import json
import requests

data = {
    "userId": 5,
    "instaUserName": "Dheeraj_joshi2006",
    "instaPassword": "dheeraj009",
    "country": "India",
    "state": "Madhya Pradesh",
    "city": "Indore",
    "timeoffset": "+5",
    "type": "web"
}

# Set the headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

# Send the request
response = requests.post("http://127.0.0.1:5000/login-insta", json=data, headers=headers)

# Print the response
print(response.status_code)
print(response.json())
