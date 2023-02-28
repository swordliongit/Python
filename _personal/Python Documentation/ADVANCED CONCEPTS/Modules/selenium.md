
**Initializing web driver**
```python
from selenium import webdriver

driver = webdriver.Chrome("chromedriverpath/chromedriver")
```
**Making the browser silent**
```python
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver", options=chrome_options)
```
---
**Opening a url**
```python
driver.get(url)
```
---
***Finding a specific element in the page**
```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "username")
```
**Waiting until finding the element**
```python
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
```
---
**Clearing a field element and changing it**
```python
from selenium.webdriver.common.keys import Keys

element = driver.find_element(By.ID, "username") #By.ID, By.NAME, By.CSS_SELECTOR
element.clear()
element.send_keys(username)
```
---
**Clicking on an element after finding it**
```python
element.click()
```
**Defensive clicking, will throw exception if the element is not clickable after 10 seconds**
```python
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
```
---
**How to get the text attribute of an element**
```python
field_text = driver.find_element(By.ID, "username").text
```
**How to get any attribute of an element**
```python
value = element.get_attribute('value')
```
---
**How to know if a checkbox element was checked or not**
```python
is_fieldselected = True if checbox_element.is_selected() else False
```
---
**How to accept page alert pop-ups**
```python
from selenium.webdriver.common.alert import Alert

WebDriverWait(driver, 10).until(lambda d: Alert(d)).accept()
```