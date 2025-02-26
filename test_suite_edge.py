# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from ActionPage.ActionsPage import (InvalidLoginActionsPage, ValidLoginActionsPage, ClickAddNewContact1ActionsPage,
#                                     AddNewContact1ActionsPage, ClickAddNewContact2ActionsPage, AddNewContact2ActionsPage,
#                                     ClickAddNewContact3ActionsPage, AddNewContact3ActionsPage, ClickAddNewContact4ActionsPage,
#                                     AddNewContact4ActionsPage, ClickAddNewContact5ActionsPage, AddNewContact5ActionsPage,
#                                     ClickAddNewContact6ActionsPage, AddNewContact6ActionsPage, ClickAddNewContact7ActionsPage,
#                                     AddNewContact7ActionsPage, ClickAddNewContact8ActionsPage, AddNewContact8ActionsPage,
#                                     ClickAddNewContact9ActionsPage, AddNewContact9ActionsPage, ClickAddNewContact10ActionsPage,
#                                     AddNewContact10ActionsPage)
#
#
# @pytest.fixture(scope="module")
# def driver_setup():
#     chrome_options = Options()
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture(scope="module")
# def login(driver_setup):
#     driver = driver_setup
#     login_page = ValidLoginActionsPage(driver)
#     login_page.login_url("https://thinking-tester-contact-list.herokuapp.com/")
#     return login_page
#
#
# def test_valid_login_credentials(login):
#     login.enter_username("123QQ@gmail.com")
#     login.enter_password("12345aaaaa")
#     login.click_submit_button1()
#
#
# def test_add_new_contact1_button(login):
#     add_contact = ClickAddNewContact1ActionsPage(login.driver)
#     add_contact.click_add_new_contact1_button()
#
#
# def test_add_new_contact1_info(login):
#     contact_info = AddNewContact1ActionsPage(login.driver)
#     contact_info.enter_contact_firstname("Paul")
#     contact_info.enter_contact_lastname("Pualo")
#     contact_info.enter_contact_birthday("1990-01-01")
#     contact_info.enter_contact_email("1C1@gmail.com")
#     contact_info.enter_contact_phone("1234567")
#     contact_info.enter_contact_street_address1("Shyllor")
#     contact_info.enter_contact_street_address2("Groove")
#     contact_info.enter_contact_city("Lagos")
#     contact_info.enter_contact_state("Lag")
#     contact_info.enter_contact_postal_code("3456")
#     contact_info.enter_contact_country("Nigeria")
#     contact_info.click_submit_button()
#
#
# def test_click_add_contact2_button(login):
#     add_contact = ClickAddNewContact2ActionsPage(login.driver)
#     add_contact.click_add_new_contact2_button()
#
#
# def test_click_add_contact2_info(login):
#     contact_info = ClickAddNewContact2ActionsPage(login.driver)
#     contact_info.enter_contact_firstname("Abdul")
#     contact_info.enter_contact_lastname("Abduluo")
#     contact_info.enter_contact_birthday("1992-01-01")
#     contact_info.enter_contact_email("2C1@gmail.com")
#     contact_info.enter_contact_phone("1234567")
#     contact_info.enter_contact_street_address1("Shyllor")
#     contact_info.enter_contact_street_address2("Groove")
#     contact_info.enter_contact_city("Lagos")
#     contact_info.enter_contact_state("Lag")
#     contact_info.enter_contact_postal_code("1234")
#     contact_info.enter_contact_country("Nigeria")
#     contact_info.click_submit_button()
#
#
# # def test_click_add_contact3_button(login1):
# #     addnewcontact3 = ClickAddNewContact3ActionsPage(login1.driver)
# #     addnewcontact3.click_add_new_contact3_button()
# #
# #
# # def test_click_add_contact3_info(login1):
# #     contact3_info = ClickAddNewContact3ActionsPage(login1.driver)
# #     contact3_info.enter_contact3_firstname("Udoka")
# #     contact3_info.enter_contact3_lastname("Udokalo")
# #     contact3_info.enter_contact3_birthday("1993-01-01")
# #     contact3_info.enter_contact3_email("3C1@gmail.com")
# #     contact3_info.enter_contact3_phone("1234567")
# #     contact3_info.enter_contact3_street_address1("Shyllor")
# #     contact3_info.enter_contact3_street_address2("Groove")
# #     contact3_info.enter_contact3_city("Lagos")
# #     contact3_info.enter_contact3_state("Lag")
# #     contact3_info.enter_contact3_postal_code("12")
# #     contact3_info.enter_contact3_country("Nigeria")
# #     contact3_info.click_submit_button()
# #
# #
# # def test_click_add_contact4_button(login1):
# #     addnewcontact4 = ClickAddNewContact4ActionsPage(login1.driver)
# #     addnewcontact4.click_add_new_contact4_button()
# #
# #
# # def test_click_add_contact4_info(login1):
# #     contact4_info = ClickAddNewContact4ActionsPage(login1.driver)
# #     contact4_info.enter_contact4_firstname("Bola")
# #     contact4_info.enter_contact4_lastname("Baloo")
# #     contact4_info.enter_contact4_birthday("1994-01-01")
# #     contact4_info.enter_contact4_email("4C1@gmail.com")
# #     contact4_info.enter_contact4_phone("1234567")
# #     contact4_info.enter_contact4_street_address1("Shyllor")
# #     contact4_info.enter_contact4_street_address2("Groove")
# #     contact4_info.enter_contact4_city("Lagos")
# #     contact4_info.enter_contact4_state("Lag")
# #     contact4_info.enter_contact4_postal_code("12")
# #     contact4_info.enter_contact4_country("Nigeria")
# #     contact4_info.click_submit_button()
# #
# #
# # def test_click_add_contact5_button(login1):
# #     addnewcontact5 = ClickAddNewContact5ActionsPage(login1.driver)
# #     addnewcontact5.click_add_new_contact4_button()
# #
# #
# # def test_click_add_contact5_info(login1):
# #     contact5_info = ClickAddNewContact5ActionsPage(login1.driver)
# #     contact5_info.enter_contact5_firstname("Bolaji")
# #     contact5_info.enter_contact5_lastname("Bolajilo")
# #     contact5_info.enter_contact5_birthday("1995-01-01")
# #     contact5_info.enter_contact5_email("5C1@gmail.com")
# #     contact5_info.enter_contact5_phone("1234567")
# #     contact5_info.enter_contact5_street_address1("Shyllor")
# #     contact5_info.enter_contact5_street_address2("Groove")
# #     contact5_info.enter_contact5_city("Lagos")
# #     contact5_info.enter_contact5_state("Lag")
# #     contact5_info.enter_contact5_postal_code("12")
# #     contact5_info.enter_contact5_country("Nigeria")
# #     contact5_info.click_submit_button()
# #
# #
# # def test_click_add_contact6_button(login1):
# #     addnewcontact6 = ClickAddNewContact6ActionsPage(login1.driver)
# #     addnewcontact6.click_add_new_contact6_button()
# #
# #
# # def test_click_add_contact6_info(login1):
# #     contact6_info = ClickAddNewContact5ActionsPage(login1.driver)
# #     contact6_info.enter_contact6_firstname("Mike")
# #     contact6_info.enter_contact6_lastname("Miko")
# #     contact6_info.enter_contact6_birthday("1996-01-01")
# #     contact6_info.enter_contact6_email("6C1@gmail.com")
# #     contact6_info.enter_contact6_phone("1234567")
# #     contact6_info.enter_contact6_street_address1("Shylock")
# #     contact6_info.enter_contact6_street_address2("Groove")
# #     contact6_info.enter_contact6_city("Lagos")
# #     contact6_info.enter_contact6_state("Lag")
# #     contact6_info.enter_contact6_postal_code("12")
# #     contact6_info.enter_contact6_country("Nigeria")
# #     contact6_info.click_submit_button()
# #
# #
# # def test_click_add_contact7_button(login1):
# #     addnewcontact7 = ClickAddNewContact7ActionsPage(login1.driver)
# #     addnewcontact7.click_add_new_contact7_button()
# #
# #
# # def test_click_add_contact7_info(login1):
# #     contact7_info = ClickAddNewContact7ActionsPage(login1.driver)
# #     contact7_info.enter_contact7_firstname("Mike")
# #     contact7_info.enter_contact7_lastname("Miko")
# #     contact7_info.enter_contact7_birthday("1997-01-01")
# #     contact7_info.enter_contact7_email("7C1@gmail.com")
# #     contact7_info.enter_contact7_phone("1234567")
# #     contact7_info.enter_contact7_street_address1("Shylock")
# #     contact7_info.enter_contact7_street_address2("Groove")
# #     contact7_info.enter_contact7_city("Lagos")
# #     contact7_info.enter_contact7_state("Lag")
# #     contact7_info.enter_contact7_postal_code("12")
# #     contact7_info.enter_contact7_country("Nigeria")
# #     contact7_info.click_submit_button()
# #
# #
# # def test_click_add_contact8_button(login1):
# #     addnewcontact7 = ClickAddNewContact7ActionsPage(login1.driver)
# #     addnewcontact7.click_add_new_contact7_button()
# #
# #
# # def test_click_add_contact8_info(login1):
# #     contact8_info = ClickAddNewContact8ActionsPage(login1.driver)
# #     contact8_info.enter_contact8_firstname("Mike")
# #     contact8_info.enter_contact8_lastname("Miko")
# #     contact8_info.enter_contact8_birthday("1997-01-01")
# #     contact8_info.enter_contact8_email("7C1@gmail.com")
# #     contact8_info.enter_contact8_phone("1234567")
# #     contact8_info.enter_contact8_street_address1("Shylock")
# #     contact8_info.enter_contact8_street_address2("Groove")
# #     contact8_info.enter_contact8_city("Lagos")
# #     contact8_info.enter_contact8_state("Lag")
# #     contact8_info.enter_contact8_postal_code("12")
# #     contact8_info.enter_contact8_country("Nigeria")
# #     contact8_info.click_submit_button()
# #
# #
# # def test_click_add_contact9_button(login1):
# #     addnewcontact9 = ClickAddNewContact9ActionsPage(login1.driver)
# #     addnewcontact9.click_add_new_contact9_button()
# #
# #
# # def test_click_add_contact9_info(login1):
# #     contact9_info = ClickAddNewContact9ActionsPage(login1.driver)
# #     contact9_info.enter_contact9_firstname("Kunle")
# #     contact9_info.enter_contact9_lastname("Kunlo")
# #     contact9_info.enter_contact9_birthday("1999-01-01")
# #     contact9_info.enter_contact9_email("9C1@gmail.com")
# #     contact9_info.enter_contact9_phone("1234567")
# #     contact9_info.enter_contact9_street_address1("Shylock")
# #     contact9_info.enter_contact9_street_address2("Groove")
# #     contact9_info.enter_contact9_city("Lagos")
# #     contact9_info.enter_contact9_state("Lag")
# #     contact9_info.enter_contact9_postal_code("12")
# #     contact9_info.enter_contact9_country("Nigeria")
# #     contact9_info.click_submit_button()
# #
# #
# # def test_click_add_contact10_button(login1):
# #     addnewcontact10 = ClickAddNewContact10ActionsPage(login1.driver)
# #     addnewcontact10.click_add_new_contact9_button()
# #
# #
# # def test_click_add_contact10_info(login1):
# #     contact10_info = ClickAddNewContact10ActionsPage(login1.driver)
# #     contact10_info.enter_contact10_firstname("Joey")
# #     contact10_info.enter_contact10_lastname("Joeyo")
# #     contact10_info.enter_contact10_birthday("1910-01-01")
# #     contact10_info.enter_contact10_email("10C1@gmail.com")
# #     contact10_info.enter_contact10_phone("1234567")
# #     contact10_info.enter_contact10_street_address1("Shylock")
# #     contact10_info.enter_contact10_street_address2("Groove")
# #     contact10_info.enter_contact10_city("Lagos")
# #     contact10_info.enter_contact10_state("Lag")
# #     contact10_info.enter_contact10_postal_code("12")
# #     contact10_info.enter_contact10_country("Nigeria")
# #     contact10_info.click_submit_button()
