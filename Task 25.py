from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Create a new instance of Chrome WebDriver
driver = webdriver.Chrome()

# Open the IMDb search page
driver.get("https://www.imdb.com/search/name/")

try:
    # Use explicit wait to wait for the element with ID "name" to be visible
    name_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "name")))
    # Fill the data in the input box
    name_input.send_keys("Sakila Banu")

    # Use explicit wait to wait for the element with ID "birth_month" to be visible
    birth_month_dropdown = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "birth_month")))
    # Fill the data in the birth month dropdown
    birth_month_dropdown.send_keys("June")

    # Use explicit wait to wait for the element with ID "birth_day" to be visible
    birth_day_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "birth_day")))
    # Fill the data in the birth day input box
    birth_day_input.send_keys("12")

    # Use explicit wait to wait for the element with ID "birth_year" to be visible
    birth_year_input = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "birth_year")))
    # Fill the data in the birth year input box
    birth_year_input.send_keys("1989")

    # Select gender
    gender_select = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "gender")))
    gender_select.send_keys("Female")

    # Click the search button
    driver.find_element(By.ID, "search").click()

    # Wait for the search results to load with an increased timeout
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "findHeader")))
except TimeoutException as e:
    print("Timeout occurred while waiting for search results:", e)
except Exception as e:
    print("An error occurred:", e)

# Wait for the search results to load
try:
    # Wait for the search results to load with an increased timeout
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'findHeader')]")))
except TimeoutException as e:
    print("Timeout occurred while waiting for search results:", e)
except Exception as e:
    print("An error occurred:", e)

# Print the title of the search results page
print("Search results page title:", driver.title)

# Close the browser
driver.quit()

