
---

# Day 1

```markdown
# Selenium Day 1 Notes

## Introduction
Today we started working with Selenium WebDriver using Python. Selenium is a tool used to automate web browsers. Below are the notes and explanations from the first day of practice.

---

## Basic Web Navigation

### Example 1: Opening a Website

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://cydeo.com/")
driver.quit()
```

### Explanation:
- `webdriver.Chrome()`: Launches a new Chrome browser window.
- `driver.get("https://cydeo.com/")`: Navigates to the Cydeo website.
- `driver.quit()`: Closes the entire browser and ends the session.

---

## Example 2: Basic Browser Operations

```python
from selenium import webdriver

# Create an instance of Chrome browser
driver = webdriver.Chrome()

# Maximize the window size
driver.maximize_window()

# Navigate to the specified URL
driver.get("https://www.tesla.com")
```

### Explanation:
- `driver.maximize_window()`: Maximizes the browser window for better visibility.
- `driver.get(...)`: Opens the specified website.

```python
# Get the current URL
print(driver.current_url)

# Get the page title
print(driver.title)
```

### Explanation:
- `driver.current_url`: Returns the current URL as a string.
- `driver.title`: Returns the title of the current page.

---

## Navigating Between Pages

```python
# Navigate back in browser history
driver.back()

# Navigate forward in browser history
driver.forward()

# Refresh the browser
driver.refresh()
```

### Explanation:
- `driver.back()`: Navigates back to the previous page.
- `driver.forward()`: Goes forward to the next page.
- `driver.refresh()`: Reloads the current page.

---

## Navigating to a New Website

```python
driver.get("https://www.google.com")

# Print current URL and title
print(driver.current_url)
print(driver.title)
```

### Explanation:
- Navigates to Google.
- Prints the URL and title of the Google homepage.

---

## More Navigation

```python
# Navigate back and forward again
driver.back()
driver.forward()
driver.refresh()
```

---

## Closing the Browser

```python
# Close the current tab
driver.close()

# Quit the browser and end the session
driver.quit()
```

### Explanation:
- `driver.close()`: Closes the current tab or window.
- `driver.quit()`: Closes all tabs and quits the WebDriver session entirely.

---

## Summary

Today we learned how to:
- Launch and close a browser using Selenium.
- Navigate to a website.
- Use browser navigation methods like back, forward, and refresh.
- Get the title and URL of a page.
- Maximize the browser window.

This is the foundation for browser automation. In the coming days, we will interact with elements, fill out forms, and run automated tests.


