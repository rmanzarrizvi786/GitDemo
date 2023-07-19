from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("file:///C:/Users/cgv758/OneDrive%20-%20AFRY/Desktop/Python%20Automation%20Testing/Ex_Files_Python_Automation_Testing_Upd/Exercise%20Files/CH02/html_code_02.html")
content = driver.find_element(By.CLASS_NAME, 'content')
print("My class element is:")
print(content)
driver.close()
