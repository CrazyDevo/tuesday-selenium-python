
from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.cydeo.com/")

actual_title=driver.title
expected_title="Practice"

if actual_title==expected_title:
    print("SUCCESS")
else:
    print("FAILED")

expected_url_contains="cydeo"
actual_url=driver.current_url

if expected_url_contains in actual_url:
    print("SUCCESS")
else:
    print("FAILED")