import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LocatorPage.LocatorsPage import InvalidLoginLocatorsPage


class InvalidLoginActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, name):
        enter_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.enter_username))
        enter_username.send_keys(name)

    def enter_password(self, word):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.enter_password))
        enter_password.send_keys(word)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.click_submit_button))
        click_submit_button.click()
        time.sleep(3)
