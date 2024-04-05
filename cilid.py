from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Google homepage
driver.get("http://www.google.com")

# Wait for the 'About' link to be clickable and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "About"))).click()

# Switch to the new window and verify the title contains 'About Google'
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[-1])
assert "About Google" in driver.title

# Close the new window and switch back to the original window
driver.close()
driver.switch_to.window(driver.window_handles[0])

# End the WebDriver session
driver.quit()
