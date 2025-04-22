from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.cydeo.com")
ab_test=driver.find_element(By.LINK_TEXT,"A/B Testing")
ab_test.click()
#header=driver.find_element(By.XPATH,"//h3")
#header=driver.find_element(By.TAG_NAME,"h3")
header=driver.find_element(By.CSS_SELECTOR,"h3")
print(driver.current_url)
print(header.text)

