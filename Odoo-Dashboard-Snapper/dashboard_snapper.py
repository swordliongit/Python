from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import time


def run():

    # Initialize the Chrome driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open the Odoo dashboard page
        driver.get("https://panel.xsarj.com/web/login")
        # Log in if necessary
        username = driver.find_element(By.NAME, 'login')
        password = driver.find_element(By.NAME, 'password')
        username.send_keys('info@autoronics.com')
        password.send_keys('demo')
        driver.find_element(By.XPATH, '//*[@id="wrapwrap"]/main/div/form/div[3]/button[1]').click()

        driver.get('https://panel.xsarj.com/web#menu_id=389&ks_dashboard_id=12&action=869&cids=1')
        print(driver.current_url)

        # Wait for the dashboard to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="125"]/div[2]/div[1]')
            )  # Replace with the actual element ID or suitable locator
        )

        # Find the filter menu
        filter_button = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div/div/div/button'
        )  # Replace with the actual element ID or suitable locator
        filter_button.click()

        # Select options from the dropdown menus
        field_selector = Select(driver.find_element(By.CSS_SELECTOR, '.ks_custom_filter_field_selector'))
        field_selector.select_by_visible_text('Kişi/Kurum (Purchase Order)')  # Adjust the visible text as needed

        filter_input = driver.find_element(By.XPATH, '//*[@id="ks_dn_custom_filters_container"]/div/span/input')
        filter_input.click()
        filter_input.send_keys('Pamukkale')
        apply_filter_button = driver.find_element(
            By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div/div/div/div/div[1]/div/div[2]/button[1]'
        )  # Replace with the actual element ID or suitable locator
        apply_filter_button.click()
        # Close the filter button, new dashboard is applied, grab the snapshot next
        filter_button.click()
        time.sleep(5)  # import time

        screenshot_path = 'dashboard_screenshot.png'

        required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(required_width, required_height)
        # driver.save_screenshot(path)  # has scrollbar
        driver.find_element_by_tag_name('body').screenshot(screenshot_path)  # avoids scrollbar
        # Take a screenshot
        # driver.save_screenshot(screenshot_path)

        # print(f'Screenshot saved to {screenshot_path}')
    finally:
        driver.quit()


run()
