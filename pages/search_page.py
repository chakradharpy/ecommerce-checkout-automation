import time
from locators.locator import Setlocator
from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver) 
    
    def go_to_products(self):
        self.click(Setlocator.product_path)
    
    def input_product(self, data):
        self.enter_text(Setlocator.input_product_path, data["product_name"])
    
    def search_product(self):
        self.click(Setlocator.search_path)
        self.driver.execute_script("window.scrollBy(0, 550);")
        time.sleep(5)

    def verify_product_visible(self):
        return self.wait_for_element(Setlocator.items_path)
        