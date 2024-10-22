import pytest
from selenium import webdriver
from ActionPage.ActionsPage import InvalidLoginActionsPage


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
    login_page = ActionPage(driver)
    login_page.login_url("https://thinking-tester-contact-list.herokuapp.com/")
    return login_page


def test_invalid_login_page_contact_web_app(login):
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_submit_button()