from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Open the jewelry e-commerce website
driver.get("https://example-jewelry.com")

# Find the search bar and enter a search query
search_box = driver.find_element_by_id("searchBox")
search_query = "diamond necklace"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for search results to load (using explicit wait)
wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))

# Print the number of search results
print(f"Number of search results: {len(search_results)}")

# Verify search result titles contain the search query
for result in search_results:
    title = result.find_element_by_class_name("product-title").text
    assert search_query.lower() in title.lower(), f"Search query not found in result: {title}"

# Close the browser
driver.quit()
