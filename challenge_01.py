from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://seleniumhq.org")

# Wait for the element with ID "q" to be visible
wait = WebDriverWait(driver, 30)
element_id = wait.until(EC.visibility_of_element_located((By.ID, 'q')))
print(element_id)

element_name = driver.find_element(By.NAME, 'q')
print(element_name)

heading_xpath = driver.find_element(By.XPATH, "//*[@id='mainContent']/h2[1]")
print(heading_xpath)

# Wait for the element with class name "selenium.sponsors" to be visible
element_classname = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.selenium.sponsors')))
print(element_classname)

driver.close()
