from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Open the Chrome browser.
driver=webdriver.Chrome()
# 2. Maximize the Chrome browser window.
driver.maximize_window()
# 3. Navigate to the registration form page.(https://practice.cydeo.com/registration_form)
driver.get("https://practice.cydeo.com/registration_form")
# 4. Locate the header element.
header_element=driver.find_element(By.TAG_NAME,"h2")
# 5. Get the text of the header.
actual_text_of_header=header_element.text
# 6. Compare the actual header text with the expected text.
expected_header="Registration form"
# 7. Print a message if the header text is correct.
if actual_text_of_header==expected_header:
    print("Header Text Is Correct")

# 8. Locate the first name input field.
first_name_input=driver.find_element(By.CSS_SELECTOR,"input[name='firstname']")
# 9. Get the value of its placeholder attribute.
actual_place_holder_text=first_name_input.get_attribute("placeholder")

# 10. Compare the actual placeholder value with the expected one.
expected_place_holder="first name"
# 11. Print whether the placeholder verification passed or failed.
if actual_place_holder_text==expected_place_holder:
    print("PASSED")
else:
    print("FAILED")
# 12. Close the browser.
driver.close()