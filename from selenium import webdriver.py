from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the URL for the login page
login_url = 'https://test.beeznests.com/login'

# Start a web driver and navigate to the login page
driver = webdriver.Chrome()
driver.get(login_url)

# Find the username and password input fields
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")

# Enter the login credentials
username_input.send_keys("your_username")
password_input.send_keys("your_password")

# Submit the form
password_input.send_keys(Keys.RETURN)

# Check if the login was successful
# ...

# Close the web driver
driver.close()
