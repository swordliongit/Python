# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import os
from datetime import datetime

# import chromedriver_autoinstaller

DEBUG = True


class WebCrawler:
    driver: webdriver.Chrome = None
    url = "https://identity.jollytur.ws/"
    scopecode = "PEN333"
    username = "kanal@snapturizm.com.tr"
    passwd = "snap23"
    year = ""
    month = ""
    day = ""
    option = ""

    # ANSI colors for DEBUG
    c = (
        "\033[0m",  # End of color
        "\033[36m",  # Cyan
        "\033[91m",  # Red
        "\033[35m",  # Magenta
    )

    def __init__(self, date_selection: datetime, option):
        self.year = str(date_selection.year)
        self.month = str(date_selection.month)
        self.day = str(date_selection.day)
        self.option = option
        if DEBUG:
            print(self.year, self.month, self.day, self.option)

    def init_crawler(self) -> None:
        if DEBUG:
            print(self.c[3] + os.getcwd())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        # self.driver = webdriver.Chrome(options=options)

    def exit(self) -> None:
        self.driver.close()

    def login(self) -> None:
        self.driver.get(self.url)  # open the url
        self.driver.find_element(By.ID, "ScopeCode").send_keys(self.scopecode)
        self.driver.find_element(By.ID, "Username").send_keys(self.username)
        self.driver.find_element(By.NAME, "Password").send_keys(self.passwd)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div > div > div > div.login-right > div > form > div.buttons.align-left > input",
        ).click()  # login button

    def logged_out(self) -> bool:
        try:
            self.driver.find_element(By.ID, "Username")
        except:
            return False
        else:
            return True

    def crawl(self):
        # self.driver.maximize_window()
        # Extranet Modülü
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "body > div > div > div > div.login-right > nav > a:nth-child(1)",
                )
            )
        ).click()
        if DEBUG:
            print(self.c[1] + self.driver.title)
        # Extranet Giriş
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "body > div > div > div.login.box.login-v2 > div > div > a.btn.btn-block.grd-btn.success-action",
                )
            )
        ).click()
        if DEBUG:
            print(self.c[1] + self.driver.title)
        # Kontenjan
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#MainMenu > div.list-group.panel.ps-container.ps-theme-default > a:nth-child(7)",
                )
            )
        ).click()
        if DEBUG:
            print(self.c[1] + self.driver.title)

        # actions = ActionChains(self.driver)
        # # Move the mouse pointer to the right by a certain distance (e.g., 100 pixels)
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (
        #             By.CSS_SELECTOR,
        #             "body > div.menu-overlay",
        #         )
        #     )
        # )
        # actions.click(element).perform()
        # # actions.move_to_element(element).move_by_offset(0, 150).click().perform()
        # if DEBUG:
        #     print(self.c[2] + "Hid Overlay")

        # Click on overlay to dismiss it, we need this for silent browser
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "body > div.menu-overlay",
                )
            )
        ).click()

        # Year Selection
        yearlist = Select(self.driver.find_element(By.CSS_SELECTOR, "#Year"))
        yearlist.select_by_value(self.year)
        if DEBUG:
            print(self.c[2] + "Year Selected")

        sleep(1.5)

        # + - Standart Oda Toggle
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#searchResultHotelRoomQuota > div > div > div.panel-group.grd-collapse-group > div > div.panel-heading.collapsed > h4 > a",
                )
            )
        ).click()
        if DEBUG:
            print(self.c[2] + "Standart Oda Toggled")

        sleep(1.5)

        # Month Selection
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#_1_9027_{self.month}"))).click()
            if DEBUG:
                print(self.c[2] + "Month Selected")
        except:
            print(self.c[2] + "Kontenjan Bulunamadı")
            return False

        # Day Selection
        text = (
            WebDriverWait(self.driver, 10)
            .until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        f"#quotaPanelForMonth__1_9027 > div > div > div > div:nth-child({str(int(self.day)+1)}) > div.quotaBox.currentStatus",
                    )
                )
            )
            .text
        )
        if DEBUG:
            print(self.c[2] + "Day Selected")
        if DEBUG:
            print(self.c[2] + "Current Status: " + text)

        # Status Selection
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    f"#quotaPanelForMonth__1_9027 > div > div > div > div:nth-child({str(int(self.day)+1)}) > div.quotaBox.status > div > span > span.selection > span",
                )
            )
        ).click()
        if DEBUG:
            print(self.c[2] + "Status Drop Down Activated")

        sleep(1)

        # Define the Xpath for the wrapper element
        wrapper_xpath = f"//*[@id='quotaPanelForMonth__1_9027']/div/div/div/div[{str(int(self.day)+1)}]/div[7]/div"
        # Find the wrapper element
        wrapper_element = self.driver.find_element(By.XPATH, wrapper_xpath)
        # Find the <select> element within the wrapper
        select_element = wrapper_element.find_element(By.TAG_NAME, "select")
        selection_list = Select(select_element)

        value = 0
        if self.option == "Satışa Açık":
            value = 0
        elif self.option == "Satışı Durdur":
            value = 2
        elif self.option == "Sor Sat":
            value = 3
        elif self.option == "Serbest Satış  (Girilen deadline bile olsa satışa açacaktır)":
            value = 1
        selection_list.select_by_value(str(value))
        if DEBUG:
            print(self.c[2] + "Status Modified")

        # Save Button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#searchResultHotelRoomQuota > div > div > div.panel-group.grd-collapse-group > div > div.panel-heading > div.align-right.col-buttons > a",
                )
            )
        ).click()
        if DEBUG:
            print(self.c[2] + "Status Saved")
        self.exit()


def buttonAction() -> None:
    date_selection = datetime(2023, 10, 31)
    crawler = WebCrawler(date_selection, "Satışa Açık")
    if not crawler.driver:
        crawler.init_crawler()
    crawler.login()
    if not crawler.logged_out():
        crawler.crawl()


def main():
    buttonAction()


if __name__ == "__main__":
    main()
