import requests

# Define the URL for the login page
login_url = 'https://test.beeznests.com/login'

# Define the login credentials
payload = {
    'username': 'madtuzzi@gmail.com',
    'password': 'Hatter$1982'
}

# Send a post request to the login page with the payload
response = requests.post(login_url, data=payload)

# Check if the login was successful
