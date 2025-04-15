from selenium import webdriver

driver=webdriver.Firefox()
driver.maximize_window()

driver.get("https://google.com")
print(driver.current_url)

driver.get("https://youtube.com")

print(driver.current_url)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.refresh()

driver.quit()