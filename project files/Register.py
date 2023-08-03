from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Open the sign-up page
driver.get("https://bluestone.com/signup")

# Find the registration form fields and enter information
username_field = driver.find_element_by_id("username")
email_field = driver.find_element_by_id("email")
password_field = driver.find_element_by_id("password")

username_field.send_keys("new_username")
email_field.send_keys("test@example.com")
password_field.send_keys("securepassword")

# Find and click the sign-up button
signup_button = driver.find_element_by_id("signupButton")
signup_button.click()

# Wait for a few seconds to observe the result (you might want to use explicit waits here)
time.sleep(120)

# Verify the expected outcome (successful registration, error message, etc.)
if "Welcome" in driver.title:
    print("Sign-up successful!")
else:
    print("Sign-up failed!")

# Close the browser
driver.quit()
