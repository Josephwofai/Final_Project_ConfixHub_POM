import time

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from LocatorPage.LocatorsPage import (InvalidLoginLocatorsPage, ValidLoginLocatorsPage,
                                      ClickAddNewContact1LocatorsPage, AddNewContact1LocatorsPage,
                                      ClickAddNewContact2LocatorsPage, AddNewContact2LocatorsPage,
                                      ClickAddNewContact3LocatorsPage, AddNewContact3LocatorsPage,
                                      ClickAddNewContact4LocatorsPage, AddNewContact4LocatorsPage,
                                      ClickAddNewContact5LocatorsPage, AddNewContact5LocatorsPage,
                                      ClickAddNewContact6LocatorsPage, AddNewContact6LocatorsPage,
                                      ClickAddNewContact7LocatorsPage, AddNewContact7LocatorsPage,
                                      ClickAddNewContact8LocatorsPage, AddNewContact8LocatorsPage,
                                      ClickAddNewContact9LocatorsPage, AddNewContact9LocatorsPage,
                                      ClickAddNewContact10LocatorsPage, AddNewContact10LocatorsPage, )


class InvalidLoginActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_invalid_username(self, name):
        enter_invalid_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.enter_invalid_username))
        enter_invalid_username.send_keys(name)
        time.sleep(3)

    def enter_invalid_password(self, word):
        enter_invalid_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.enter_invalid_password))
        enter_invalid_password.send_keys(word)
        time.sleep(3)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.click_submit_button))
        click_submit_button.click()
        time.sleep(3)


class ValidLoginActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, name):
        enter_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.enter_username))
        enter_username.send_keys(name)
        time.sleep(3)

    def enter_password(self, word):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.enter_password))
        enter_password.send_keys(word)
        time.sleep(3)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.click_submit_button))
        click_submit_button.click()
        time.sleep(3)


class ClickAddNewContact1ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact1_button(self):
        click_add_new_contact1_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact1LocatorsPage.Click_Add_New_Contact1_Button))
        click_add_new_contact1_button.click()
        time.sleep(3)


class AddNewContact1ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact1_first_name(self, name):
        enter_contact1_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_first_name))
        enter_contact1_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact1_lastname(self, lastname):
        enter_contact1_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_lastname))
        enter_contact1_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact1_birthday(self, name):
        enter_contact1_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_birthday))
        enter_contact1_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact1_email(self, mail):
        enter_contact1_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_email))
        enter_contact1_email.send_keys(mail)
        time.sleep(3)

    def enter_contact1_phone(self, phone):
        enter_contact1_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_phone))
        enter_contact1_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact1_street_address1(self, street):
        enter_contact1_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_street_address1))
        enter_contact1_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact1_street_address2(self, address):
        enter_contact1_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_street_address2))
        enter_contact1_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact1_city(self, city):
        enter_contact1_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_city))
        enter_contact1_city.send_keys(city)
        time.sleep(3)

    def enter_contact1_state(self, state):
        enter_contact1_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_state))
        enter_contact1_state.send_keys(state)
        time.sleep(3)

    def enter_contact1_postal_code(self, code):
        enter_contact1_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_postal_code))
        enter_contact1_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact1_country(self, country):
        enter_contact1_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_country))
        enter_contact1_country.send_keys(country)
        time.sleep(3)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.click_contact1_submit_button))
        click_submit_button.click()
        time.sleep(3)


class AddNewContact2ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact2_first_name(self, name):
        enter_contact2_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_first_name))
        enter_contact2_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact2_lastname(self, lastname):
        enter_contact2_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact2_lastname))
        enter_contact2_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact2_birthday(self, name):
        enter_contact2_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact2_birthday))
        enter_contact2_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact1_email(self, mail):
        enter_contact1_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_email))
        enter_contact1_email.send_keys(mail)
        time.sleep(3)

    def enter_contact1_phone(self, phone):
        enter_contact1_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_phone))
        enter_contact1_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact1_street_address1(self, street):
        enter_contact1_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_street_address1))
        enter_contact1_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact1_street_address2(self, address):
        enter_contact1_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_street_address2))
        enter_contact1_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact1_city(self, city):
        enter_contact1_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_city))
        enter_contact1_city.send_keys(city)
        time.sleep(3)

    def enter_contact1_state(self, state):
        enter_contact1_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_state))
        enter_contact1_state.send_keys(state)
        time.sleep(3)

    def enter_contact1_postal_code(self, code):
        enter_contact1_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_postal_code))
        enter_contact1_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact1_country(self, country):
        enter_contact1_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.enter_contact1_country))
        enter_contact1_country.send_keys(country)
        time.sleep(3)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact1LocatorsPage.click_contact1_submit_button))
        click_submit_button.click()
        time.sleep(3)
