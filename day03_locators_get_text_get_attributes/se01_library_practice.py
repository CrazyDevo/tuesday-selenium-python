from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 1. Open the Chrome browser.
driver=webdriver.Chrome()
# 2. Maximize the browser window.
driver.maximize_window()
# 3. Navigate to the library login page.(https://app.seamlessly.net/index.php/login)
driver.get("https://app.seamlessly.net/index.php/login")
# 4. Enter an incorrect username.
user_name_input_box=driver.find_element(By.ID,"user")
user_name_input_box.send_keys("invalid")
# 5. Enter a password.
pass_input_box=driver.find_element(By.NAME,"password")
pass_input_box.send_keys("invalid")
# 6. Click the login button.
login_button=driver.find_element(By.CSS_SELECTOR,"input[type='submit']")
login_button.click()
# 7. Wait for the error message to appear.
time.sleep(3)
# 8. Locate the error message element.
warning_message=driver.find_element(By.XPATH,"//p[@class='warning wrongPasswordMsg']")
actual_text=warning_message.text
expected_text="Wrong username or password."
# 9. Check if the error message is displayed.
if actual_text==expected_text:
    print("PASSED")

else:
    print("FAILED")


# 10. Print a message based on the visibility of the error.
# 11. Close the browser.
driver.quit()
