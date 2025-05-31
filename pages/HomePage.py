from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self,driver):
        self.driver=driver

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    no_product_message_xpath = "//input[@id='button-search']/following-sibling::p"
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()

    def retrieve_no_product_message(self):
        return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH,self.my_account_drop_menu_xpath).click()


    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_link_text).click()

