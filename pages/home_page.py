from locators.locator import Setlocator
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # inherit from BasePage

    def open(self):
        self.driver.get("https://automationexercise.com/")

    
