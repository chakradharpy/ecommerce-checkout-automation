import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
import json
from pages.checkout_page import CheckoutPage
import os
import sys
# 🔧 Add the root folder to sys.path so that 'pages' can be imported
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def load_test_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

@pytest.mark.usefixtures("setup")
class TestEndToEndCheckout:
    def test_end_to_end_checkout(self):
        data = load_test_data(r"C:\Users\Chakradhar.corp\Desktop\automation_task\data\test_data.json")
        

        hp = HomePage(self.driver)
        hp.open()

        sp = SearchPage(self.driver)
        sp.go_to_products()
        sp.input_product(data)
        sp.search_product()
        assert sp.verify_product_visible(), "Product not found in search results"

        cp =CartPage(self.driver)
        cp.add_to_cart()
        cp.view_cart()
        assert cp.is_product_in_cart(), "Product is not added to cart"

        assert cp.verify_cart_count(), "Cart count is not 1"


        ch = CheckoutPage(self.driver)
        ch.checkout_page()                      
        ch.user_login(data)     
        assert ch.is_checkout_loaded(), "Checkout page did not load correctly"
              
         

        # Step 5: Finalize order
        
        cp.place_order()
        cp.payment_page(data)
        cp.order_placed()
        assert cp.is_order_confirmed(), "Order confirmation not displayed"
        