
from locators.locator import Setlocator
from pages.base_page import BasePage
import time


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def checkout_page(self):
        time.sleep(2)
        self.click(Setlocator.checkout_path)
        self.click(Setlocator.login_path)
    
    def is_checkout_loaded(self):
       return self.wait_for_element(Setlocator.checkout_path_visible)
    

    
    
    def user_signup(self, data):
        self.enter_text(Setlocator.name_path, data["name"])
        self.enter_text(Setlocator.email_path, data["email"])
        time.sleep(5)
        self.click(Setlocator.signup_path)
        self.enter_text(Setlocator.password_path, data["password"])
        self.driver.execute_script("window.scrollBy(0, 550);")
    
    def address_information(self, data):
        self.enter_text(Setlocator.first_name_path, data["first_name"])
        self.enter_text(Setlocator.last_name_path, data["last_name"])
        self.enter_text(Setlocator.address_path, data["address1"])
        self.enter_text(Setlocator.state_path, data["state"])
        self.enter_text(Setlocator.city_path, data["city"])
        self.enter_text(Setlocator.zipcode_path, data["zipcode"])
        self.driver.execute_script("window.scrollBy(0, 550);")
        self.enter_text(Setlocator.mobile_path, data["mobile"])
        self.click(Setlocator.create_path)
        self.click(Setlocator.continue_button_path)
    
    def user_login(self, data):
        self.enter_text(Setlocator.login_email_path, data["email"])
        self.enter_text(Setlocator.login_password_path, data["password"])
        self.click(Setlocator.login_button)
        time.sleep(2)
        self.click(Setlocator.cart_path)


    
        
        