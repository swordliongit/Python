from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

EMAIL = ""
PASSWORD = ""

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument('--disable-application-cache')
options.add_argument('--disable-gpu')
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=~/.config/google-chrome/')
# options.add_argument("--disable-features=LockProfileCookieDatabase")
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

browser.get("https://bard.google.com/")
browser.find_element(by=By.XPATH, value='//*[@id="gb"]/div[2]/div[3]/div[1]/a').click()
browser.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(EMAIL)
browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
# get_url = browser.current_url
# print(get_url)
sleep(999)  # import time

# from bardapi import Bard

# bard = Bard(token_from_browser=True)
# res = bard.get_answer("Do you like cookies?")
# print(res['content'])
