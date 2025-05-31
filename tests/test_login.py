from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class Testlogin:
 def test_login_with_valid_credential(self):
  home_page = HomePage(self.driver)
  home_page.click_on_my_account_drop_menu()
  home_page.select_login_option()
  login_page=LoginPage(self.driver)
  login_page.enter_email_address('Manojprajapat315@gmail.com')
  login_page.enter_password('manoj796')
  login_page.click_on_login_button()

  '''
    self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    self.driver.find_element(By.LINK_TEXT,"Login").click()
    self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys("manojprajapat315@gmail.com")
    self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("manojprajat")
    self.driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()'''


 def test_login_with_invalid_email_and_valid_password_credential(self):
  home_page = HomePage(self.driver)
  home_page.click_on_my_account_drop_menu()
  home_page.select_login_option()
  login_page = LoginPage(self.driver)
  login_page.enter_email_address(self.generate_email_with_time_stamp())
  login_page.enter_password('12345')
  login_page.click_on_login_button()
  expected_warning_message ="Warning: No match for E-Mail Address and/or Password."
  assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

  '''self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
  self.driver.find_element(By.LINK_TEXT,"Login").click()
  self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(self.generate_email_with_time_stamp())
  self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("12345")
  self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
  expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
  assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__eq__(expected_warning_message)
  print('test case verified with_login_with_invalid_email_and_valid_password_credential')'''

 def test_login_with_valid_email_and_invalid_password_credential(self):
  home_page = HomePage(self.driver)
  home_page.click_on_my_account_drop_menu()
  home_page.select_login_option()
  login_page = LoginPage(self.driver)
  login_page.enter_email_address('manojprajapat315@gmail.com')
  login_page.enter_password('12345')
  login_page.click_on_login_button()
  expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
  assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

  '''self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
  self.driver.find_element(By.LINK_TEXT,"Login").click()
  self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys('manojprajapat315@gmail.com')
  self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("12345")
  self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
  expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
  assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__eq__(expected_warning_message)
  print('test case verified with_login_with_valid_email_and_invalid_password_credential')'''


 def test_login_with_without_entering_credential(self):
  home_page = HomePage(self.driver)
  home_page.click_on_my_account_drop_menu()
  home_page.select_login_option()
  login_page = LoginPage(self.driver)
  login_page.enter_email_address('')
  login_page.enter_password('')
  login_page.click_on_login_button()
  expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
  assert login_page.retrieve_warning_message().__eq__(expected_warning_message)

  '''self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
  self.driver.find_element(By.LINK_TEXT,"Login").click()
  self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys('')
  self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
  self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
  expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
  assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__eq__(expected_warning_message)
  print('test case verified _login_with_without_entering_credential')'''

 def generate_email_with_time_stamp(self):
   time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
   return "amotoori"+time_stamp+"@gmail.com"