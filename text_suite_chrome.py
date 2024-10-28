import pytest
from selenium import webdriver
from ActionPage.ActionsPage import (InvalidLoginActionsPage, ValidLoginActionsPage,
                                    ClickAddNewContact1ActionsPage, AddNewContact1ActionsPage)


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = InvalidLoginActionsPage(driver)
    login_page.login_url("https://thinking-tester-contact-list.herokuapp.com/")
    return login_page


@pytest.fixture(scope="module")
def login1(driver_setup):
    driver = driver_setup
    login_page = ValidLoginActionsPage(driver)
    login_page.login_url("https://thinking-tester-contact-list.herokuapp.com/")
    return login_page


def test_invalid_login_credentials(login):
    login.enter_invalid_username("standard_user")
    login.enter_invalid_password("secret_sauce")
    login.click_submit_button()


def test_valid_login_credentials(login1):
    login1.enter_invalid_username("123QQQ@gmail.com")
    login1.enter_invalid_password("12345aaaaa")
    login1.click_submit_button()

def test_add_new_contact1_button(login1):
    addnewcontact1 = ClickAddNewContact1ActionsPage(login1.driver)
    addnewcontact1.click_add_new_contact1_button()

def test_add_new_contact1_info(login1)
    contact1_info = AddNewContact1ActionsPage(login1.driver)
    contact1_info.enter_contact1_first_name("Paul")

