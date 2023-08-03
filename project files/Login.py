from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
login_url = "https://bluestone.com/login"
driver.get(login_url)
# Find the username and password input fields and the login button using their respective HTML attributes (IDs, names, etc.).
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "loginButton")

# Input data into the fields
username_field.send_keys("your_username")
password_field.send_keys("your_password")

# Click the login button
login_button.click()
