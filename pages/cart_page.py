import time
from locators.locator import Setlocator
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def add_to_cart(self):
        self.click(Setlocator.add_cart_path)

    def view_cart(self):
        self.click(Setlocator.view_cart)
    
    def is_product_in_cart(self):
        product_name = self.get_text(Setlocator.product_in_cart_path)
        return "Tshirt" in product_name

    
    def verify_cart_count(self):
        count = self.get_text(Setlocator.product_count_path)
        return count == "1"

    

    def place_order(self):
        self.click(Setlocator.checkout_path)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 650);")
        time.sleep(2)
        self.click(Setlocator.place_order)
        time.sleep(5)
    
    def payment_page(self, data):
        self.enter_text(Setlocator.card_name, data["cardname"])
        self.enter_text(Setlocator.card_number, data["cardnumber"])
        self.enter_text(Setlocator.cvc, data["cvcnumber"])
        self.enter_text(Setlocator.expiry_month_path, data["exp_month"])
        self.enter_text(Setlocator.expiry_year_path, data["exp_year"])

    def order_placed(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.click(Setlocator.pay_path)
        time.sleep(2)
        
    
    def is_order_confirmed(self):
        confirmation_message = self.get_text(Setlocator.order_place_path)
        return "Congratulations! Your order has been confirmed!" in confirmation_message
    
    
    

        