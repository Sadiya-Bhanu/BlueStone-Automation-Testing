from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Open the jewelry e-commerce website
driver.get("https://example-jewelry.com")

# Find and click on the "Rings" link in the navigation menu
rings_link = driver.find_element_by_link_text("Rings")
rings_link.click()

# Wait for the rings page to load (using explicit wait)
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Rings"))

# Verify the title of the page
assert "Rings" in driver.title, "Rings page title not as expected"

# Find and interact with different elements on the rings page
filter_dropdown = driver.find_element_by_id("filterDropdown")
filter_dropdown.click()

# Select a filter option (e.g., "Gold")
gold_filter_option = driver.find_element_by_xpath("//ul[@id='filterOptions']/li[contains(text(), 'Gold')]")
gold_filter_option.click()

# Wait for the filtered results to load
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item")))

# Verify that filtered results contain the chosen filter
filtered_results = driver.find_elements_by_class_name("product-item")
for result in filtered_results:
    assert "Gold" in result.text, "Filtered result does not contain 'Gold'"

# Close the browser
driver.quit()
