from datetime import datetime
import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.mark.usefixtures("setup_teardown")
class TestRegister:
 def test_Register_with_mandatory_fields(self):
    self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    self.driver.find_element(By.LINK_TEXT,"Register").click()
    self.driver.find_element(By.ID,'input-firstname').send_keys("manoj")
    self.driver.find_element(By.ID,'input-lastname').send_keys("kumhar")
    self.driver.find_element(By.ID,'input-email').send_keys(self.generate_email_with_time_stamp())
    self.driver.find_element(By.ID,'input-telephone').send_keys("9783943485")
    self.driver.find_element(By.ID,'input-password').send_keys("Manoj@796")
    self.driver.find_element(By.ID,'input-confirm').send_keys("Manoj@796")
    self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
    self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    expected_result="Your Account Has Been Created!"
    self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_result)


 def test_Register_with_all_fields(self):
    self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.ID, 'input-firstname').send_keys("manoj")
    self.driver.find_element(By.ID, 'input-lastname').send_keys("kumhar")
    self.driver.find_element(By.ID, 'input-email').send_keys(self.generate_email_with_time_stamp())
    self.driver.find_element(By.ID, 'input-telephone').send_keys("9783943485")
    self.driver.find_element(By.ID, 'input-password').send_keys("Manoj@796")
    self.driver.find_element(By.ID, 'input-confirm').send_keys("Manoj@796")
    self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    expected_result = "Your Account Has Been Created!"
    self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_result)


 def test_Register_with_duplicates_fields(self):
    self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.ID, 'input-firstname').send_keys("manoj")
    self.driver.find_element(By.ID, 'input-lastname').send_keys("kumhar")
    self.driver.find_element(By.ID, 'input-email').send_keys(self.generate_email_with_time_stamp())
    self.driver.find_element(By.ID, 'input-telephone').send_keys("9783943485")
    self.driver.find_element(By.ID, 'input-password').send_keys("Manoj@796")
    self.driver.find_element(By.ID, 'input-confirm').send_keys("Manoj@796")
    self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    expected_result ="Warning: E-Mail Address is already registered!"
    self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__eq__(expected_result)



 def test_Register_without_entering_any_fields(self):
    self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.ID, 'input-firstname').send_keys()
    self.driver.find_element(By.ID, 'input-lastname').send_keys()
    self.driver.find_element(By.ID, 'input-email').send_keys()
    self.driver.find_element(By.ID, 'input-telephone').send_keys()
    self.driver.find_element(By.ID, 'input-password').send_keys()
    self.driver.find_element(By.ID, 'input-confirm').send_keys()
    self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
    self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    expected_result = "Warning: You must agree to the Privacy Policy!"
    self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__eq__(expected_result)
    expected_first_message="First Name must be between 1 and 32 characters!"
    self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_first_message)
    expected_last_message = "Last Name must be between 1 and 32 characters!"
    self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
        expected_last_message)
    expected_email_message="E-Mail Address does not appear to be valid!"
    self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
        expected_email_message)
    expected_telephone_message="Telephone must be between 3 and 32 characters!"
    self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
        expected_telephone_message)
    expected_pasword_message="Password must be between 4 and 20 characters!"
    self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
        expected_pasword_message)


 def generate_email_with_time_stamp(self):
    time_stamp=datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "manoj"+time_stamp+"@gamail.com"

