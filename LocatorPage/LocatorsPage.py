from selenium.webdriver.common.by import By


class InvalidLoginLocatorsPage:
    enter_username = (By.ID, "email")
    enter_password = (By.ID, "password")
    click_submit_button = (By.ID, "submit")
