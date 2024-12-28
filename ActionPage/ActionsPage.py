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

    def enter_invalid_username(self, invalid_name):
        enter_invalid_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.enter_invalid_username))
        enter_invalid_username.send_keys(invalid_name)
        time.sleep(3)

    def enter_invalid_password(self, invalid_word):
        enter_invalid_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.enter_invalid_password))
        enter_invalid_password.send_keys(invalid_word)
        time.sleep(3)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(InvalidLoginLocatorsPage.click_submit_button))
        click_submit_button.click()
        time.sleep(3)


class ValidLoginActionsPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url1(self, url):
        self.driver.get(url)

    def enter_username(self, email):
        enter_username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.enter_username))
        enter_username.send_keys(email)
        time.sleep(2)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.enter_password))
        enter_password.send_keys(password)
        time.sleep(3)

    def click_submit_button1(self):
        click_submit_button1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ValidLoginLocatorsPage.click_submit_button1))
        click_submit_button1.click()
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

    def enter_contact1_firstname(self, name):
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


class ClickAddNewContact2ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact2_button(self):
        click_add_new_contact2_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact2LocatorsPage.Click_Add_New_Contact2_Button))
        click_add_new_contact2_button.click()
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
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_lastname))
        enter_contact2_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact2_birthday(self, name):
        enter_contact2_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_birthday))
        enter_contact2_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact2_email(self, mail):
        enter_contact2_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_email))
        enter_contact2_email.send_keys(mail)
        time.sleep(3)

    def enter_contact2_phone(self, phone):
        enter_contact2_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_phone))
        enter_contact2_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact2_street_address1(self, street):
        enter_contact2_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_street_address1))
        enter_contact2_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact2_street_address2(self, address):
        enter_contact2_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_street_address2))
        enter_contact2_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact2_city(self, city):
        enter_contact2_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContac21LocatorsPage.enter_contact2_city))
        enter_contact2_city.send_keys(city)
        time.sleep(3)

    def enter_contact2_state(self, state):
        enter_contact2_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_state))
        enter_contact2_state.send_keys(state)
        time.sleep(3)

    def enter_contact2_postal_code(self, code):
        enter_contact2_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_postal_code))
        enter_contact2_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact2_country(self, country):
        enter_contact2_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact2_country))
        enter_contact2_country.send_keys(country)
        time.sleep(3)

    def click_contact2_submit_button(self):
        click_contact2_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.click_contact2_submit_button))
        click_contact2_submit_button.click()
        time.sleep(3)


class ClickAddNewContact3ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact3_button(self):
        click_add_new_contact3_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact3LocatorsPage.Click_Add_New_Contact3_Button))
        click_add_new_contact3_button.click()
        time.sleep(3)


class AddNewContact3ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact3_first_name(self, name):
        enter_contact3_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_first_name))
        enter_contact3_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact3_lastname(self, lastname):
        enter_contact3_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_lastname))
        enter_contact3_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact3_birthday(self, name):
        enter_contact3_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_birthday))
        enter_contact3_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact3_email(self, mail):
        enter_contact3_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_email))
        enter_contact3_email.send_keys(mail)
        time.sleep(3)

    def enter_contact3_phone(self, phone):
        enter_contact3_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_phone))
        enter_contact3_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact3_street_address1(self, street):
        enter_contact3_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact2LocatorsPage.enter_contact3_street_address1))
        enter_contact3_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact3_street_address2(self, address):
        enter_contact3_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_street_address2))
        enter_contact3_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact3_city(self, city):
        enter_contact3_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContac31LocatorsPage.enter_contact3_city))
        enter_contact3_city.send_keys(city)
        time.sleep(3)

    def enter_contact3_state(self, state):
        enter_contact3_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_state))
        enter_contact3_state.send_keys(state)
        time.sleep(3)

    def enter_contact3_postal_code(self, code):
        enter_contact3_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_postal_code))
        enter_contact3_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact3_country(self, country):
        enter_contact3_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.enter_contact3_country))
        enter_contact3_country.send_keys(country)
        time.sleep(3)

    def click_contact3_submit_button(self):
        click_contact3_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact3LocatorsPage.click_contact3_submit_button))
        click_contact3_submit_button.click()
        time.sleep(3)


class ClickAddNewContact4ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact4_button(self):
        click_add_new_contact4_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact4LocatorsPage.Click_Add_New_Contact4_Button))
        click_add_new_contact4_button.click()
        time.sleep(3)


class AddNewContact4ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact4_first_name(self, name):
        enter_contact4_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_first_name))
        enter_contact4_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact4_lastname(self, lastname):
        enter_contact4_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_lastname))
        enter_contact4_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact4_birthday(self, name):
        enter_contact4_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_birthday))
        enter_contact4_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact4_email(self, mail):
        enter_contact4_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_email))
        enter_contact4_email.send_keys(mail)
        time.sleep(3)

    def enter_contact4_phone(self, phone):
        enter_contact4_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_phone))
        enter_contact4_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact4_street_address1(self, street):
        enter_contact4_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_street_address1))
        enter_contact4_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact4_street_address2(self, address):
        enter_contact4_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_street_address2))
        enter_contact4_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact4_city(self, city):
        enter_contact4_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContac4LocatorsPage.enter_contact4_city))
        enter_contact4_city.send_keys(city)
        time.sleep(3)

    def enter_contact4_state(self, state):
        enter_contact4_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_state))
        enter_contact4_state.send_keys(state)
        time.sleep(3)

    def enter_contact4_postal_code(self, code):
        enter_contact4_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_postal_code))
        enter_contact4_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact4_country(self, country):
        enter_contact4_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.enter_contact4_country))
        enter_contact4_country.send_keys(country)
        time.sleep(3)

    def click_contact4_submit_button(self):
        click_contact4_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact4LocatorsPage.click_contact4_submit_button))
        click_contact4_submit_button.click()
        time.sleep(3)


class ClickAddNewContact5ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact5_button(self):
        click_add_new_contact5_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact5LocatorsPage.Click_Add_New_Contact5_Button))
        click_add_new_contact5_button.click()
        time.sleep(3)


class AddNewContact5ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact5_first_name(self, name):
        enter_contact5_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_first_name))
        enter_contact5_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact5_lastname(self, lastname):
        enter_contact5_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_lastname))
        enter_contact5_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact5_birthday(self, name):
        enter_contact5_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_birthday))
        enter_contact5_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact5_email(self, mail):
        enter_contact5_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_email))
        enter_contact5_email.send_keys(mail)
        time.sleep(3)

    def enter_contact5_phone(self, phone):
        enter_contact5_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_phone))
        enter_contact5_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact5_street_address1(self, street):
        enter_contact5_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_street_address1))
        enter_contact5_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact5_street_address2(self, address):
        enter_contact5_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_street_address2))
        enter_contact5_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact5_city(self, city):
        enter_contact5_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContac5LocatorsPage.enter_contact5_city))
        enter_contact5_city.send_keys(city)
        time.sleep(3)

    def enter_contact5_state(self, state):
        enter_contact5_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_state))
        enter_contact5_state.send_keys(state)
        time.sleep(3)

    def enter_contact5_postal_code(self, code):
        enter_contact5_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_postal_code))
        enter_contact5_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact5_country(self, country):
        enter_contact5_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.enter_contact5_country))
        enter_contact5_country.send_keys(country)
        time.sleep(3)

    def click_contact5_submit_button(self):
        click_contact5_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact5LocatorsPage.click_contact5_submit_button))
        click_contact5_submit_button.click()
        time.sleep(3)


class ClickAddNewContact6ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact6_button(self):
        click_add_new_contact6_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact6LocatorsPage.Click_Add_New_Contact6_Button))
        click_add_new_contact6_button.click()
        time.sleep(3)


class AddNewContact6ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact6_first_name(self, name):
        enter_contact6_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_first_name))
        enter_contact6_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact6_lastname(self, lastname):
        enter_contact6_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_lastname))
        enter_contact6_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact6_birthday(self, name):
        enter_contact6_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_birthday))
        enter_contact6_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact6_email(self, mail):
        enter_contact6_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_email))
        enter_contact6_email.send_keys(mail)
        time.sleep(3)

    def enter_contact6_phone(self, phone):
        enter_contact6_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_phone))
        enter_contact6_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact6_street_address1(self, street):
        enter_contact6_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_street_address1))
        enter_contact6_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact6_street_address2(self, address):
        enter_contact6_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_street_address2))
        enter_contact6_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact6_city(self, city):
        enter_contact6_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_city))
        enter_contact6_city.send_keys(city)
        time.sleep(3)

    def enter_contact6_state(self, state):
        enter_contact6_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_state))
        enter_contact6_state.send_keys(state)
        time.sleep(3)

    def enter_contact6_postal_code(self, code):
        enter_contact6_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_postal_code))
        enter_contact6_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact6_country(self, country):
        enter_contact6_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.enter_contact6_country))
        enter_contact6_country.send_keys(country)
        time.sleep(3)

    def click_contact6_submit_button(self):
        click_contact6_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact6LocatorsPage.click_contact6_submit_button))
        click_contact6_submit_button.click()
        time.sleep(3)


class ClickAddNewContact7ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact7_button(self):
        click_add_new_contact7_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact7LocatorsPage.Click_Add_New_Contact7_Button))
        click_add_new_contact7_button.click()
        time.sleep(3)


class AddNewContact7ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact7_first_name(self, name):
        enter_contact7_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_first_name))
        enter_contact7_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact7_lastname(self, lastname):
        enter_contact7_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_lastname))
        enter_contact7_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact7_birthday(self, name):
        enter_contact7_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_birthday))
        enter_contact7_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact7_email(self, mail):
        enter_contact7_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_email))
        enter_contact7_email.send_keys(mail)
        time.sleep(3)

    def enter_contact7_phone(self, phone):
        enter_contact7_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_phone))
        enter_contact7_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact7_street_address1(self, street):
        enter_contact7_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_street_address1))
        enter_contact7_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact7_street_address2(self, address):
        enter_contact7_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_street_address2))
        enter_contact7_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact7_city(self, city):
        enter_contact7_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_city))
        enter_contact7_city.send_keys(city)
        time.sleep(3)

    def enter_contact7_state(self, state):
        enter_contact7_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_state))
        enter_contact7_state.send_keys(state)
        time.sleep(3)

    def enter_contact7_postal_code(self, code):
        enter_contact7_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_postal_code))
        enter_contact7_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact7_country(self, country):
        enter_contact7_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.enter_contact7_country))
        enter_contact7_country.send_keys(country)
        time.sleep(3)

    def click_contact7_submit_button(self):
        click_contact7_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact7LocatorsPage.click_contact7_submit_button))
        click_contact7_submit_button.click()
        time.sleep(3)


class ClickAddNewContact8ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact8_button(self):
        click_add_new_contact8_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact8LocatorsPage.Click_Add_New_Contact8_Button))
        click_add_new_contact8_button.click()
        time.sleep(3)


class AddNewContact8ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact8_first_name(self, name):
        enter_contact8_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_first_name))
        enter_contact8_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact8_lastname(self, lastname):
        enter_contact8_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_lastname))
        enter_contact8_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact8_birthday(self, name):
        enter_contact8_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_birthday))
        enter_contact8_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact8_email(self, mail):
        enter_contact8_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_email))
        enter_contact8_email.send_keys(mail)
        time.sleep(3)

    def enter_contact8_phone(self, phone):
        enter_contact8_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_phone))
        enter_contact8_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact8_street_address1(self, street):
        enter_contact8_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_street_address1))
        enter_contact8_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact8_street_address2(self, address):
        enter_contact8_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_street_address2))
        enter_contact8_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact8_city(self, city):
        enter_contact8_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_city))
        enter_contact8_city.send_keys(city)
        time.sleep(3)

    def enter_contact8_state(self, state):
        enter_contact8_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_state))
        enter_contact8_state.send_keys(state)
        time.sleep(3)

    def enter_contact8_postal_code(self, code):
        enter_contact8_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_postal_code))
        enter_contact8_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact8_country(self, country):
        enter_contact8_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.enter_contact8_country))
        enter_contact8_country.send_keys(country)
        time.sleep(3)

    def click_contact8_submit_button(self):
        click_contact8_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact8LocatorsPage.click_contact8_submit_button))
        click_contact8_submit_button.click()
        time.sleep(3)


class ClickAddNewContact9ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact9_button(self):
        click_add_new_contact9_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact9LocatorsPage.Click_Add_New_Contact9_Button))
        click_add_new_contact9_button.click()
        time.sleep(3)


class AddNewContact9ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact9_first_name(self, name):
        enter_contact9_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_first_name))
        enter_contact9_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact9_lastname(self, lastname):
        enter_contact9_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_lastname))
        enter_contact9_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact9_birthday(self, name):
        enter_contact9_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_birthday))
        enter_contact9_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact9_email(self, mail):
        enter_contact9_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_email))
        enter_contact9_email.send_keys(mail)
        time.sleep(3)

    def enter_contact9_phone(self, phone):
        enter_contact9_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_phone))
        enter_contact9_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact9_street_address1(self, street):
        enter_contact9_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_street_address1))
        enter_contact9_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact9_street_address2(self, address):
        enter_contact9_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_street_address2))
        enter_contact9_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact9_city(self, city):
        enter_contact9_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_city))
        enter_contact9_city.send_keys(city)
        time.sleep(3)

    def enter_contact9_state(self, state):
        enter_contact9_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_state))
        enter_contact9_state.send_keys(state)
        time.sleep(3)

    def enter_contact9_postal_code(self, code):
        enter_contact9_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presene_of_element_located(AddNewContact9LocatorsPage.enter_contact9_postal_code))
        enter_contact9_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact9_country(self, country):
        enter_contact9_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.enter_contact9_country))
        enter_contact9_country.send_keys(country)
        time.sleep(3)

    def click_contact9_submit_button(self):
        click_contact9_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact9LocatorsPage.click_contact9_submit_button))
        click_contact9_submit_button.click()
        time.sleep(3)


class ClickAddNewContact10ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_contact10_button(self):
        click_add_new_contact10_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ClickAddNewContact10LocatorsPage.Click_Add_New_Contact10_Button))
        click_add_new_contact10_button.click()
        time.sleep(3)


class AddNewContact10ActionsPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_contact10_first_name(self, name):
        enter_contact10_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_first_name))
        enter_contact10_first_name.send_keys(name)
        time.sleep(3)

    def enter_contact10_lastname(self, lastname):
        enter_contact10_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_lastname))
        enter_contact10_lastname.send_keys(lastname)
        time.sleep(3)

    def enter_contact10_birthday(self, name):
        enter_contact10_birthday = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_birthday))
        enter_contact10_birthday.send_keys(name)
        time.sleep(3)

    def enter_contact10_email(self, mail):
        enter_contact10_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_email))
        enter_contact10_email.send_keys(mail)
        time.sleep(3)

    def enter_contact10_phone(self, phone):
        enter_contact10_phone = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_phone))
        enter_contact10_phone.send_keys(phone)
        time.sleep(3)

    def enter_contact10_street_address1(self, street):
        enter_contact10_street_address1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_street_address1))
        enter_contact10_street_address1.send_keys(street)
        time.sleep(3)

    def enter_contact10_street_address2(self, address):
        enter_contact10_street_address2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_street_address2))
        enter_contact10_street_address2.send_keys(address)
        time.sleep(3)

    def enter_contact10_city(self, city):
        enter_contact10_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_city))
        enter_contact10_city.send_keys(city)
        time.sleep(3)

    def enter_contact10_state(self, state):
        enter_contact10_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_state))
        enter_contact10_state.send_keys(state)
        time.sleep(3)

    def enter_contact10_postal_code(self, code):
        enter_contact10_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_postal_code))
        enter_contact10_postal_code.send_keys(code)
        time.sleep(3)

    def enter_contact10_country(self, country):
        enter_contact10_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.enter_contact10_country))
        enter_contact10_country.send_keys(country)
        time.sleep(3)

    def click_contact10_submit_button(self):
        click_contact10_submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(AddNewContact10LocatorsPage.click_contact10_submit_button))
        click_contact10_submit_button.click()
        time.sleep(3)


class LogOutButtonActionsPage:
    def __init__(self, driver):
        self.driver = driver()

    def click_logout_button(self):
        click_logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogOutButtonLocatorsPage.click_logout_button))
        click_logout_button.click()
        time.sleep(3)
