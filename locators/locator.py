

from selenium.webdriver.common.by import By

class Setlocator:
    home_path = (By.XPATH, "(//a[@href='/'])[2]")
    product_path = (By.XPATH, "(//a[@href='/products'])")
    input_product_path = (By.XPATH, "//input[@id='search_product']")
    search_path = (By.XPATH, "//button[@id='submit_search']")
    items_path = (By.XPATH, "//div[@class='features_items']")
    add_cart_path =(By.XPATH, "(//a[@data-product-id='2'])[1]")
    view_cart = (By.XPATH, "(//a[@href='/view_cart'])[2]")
    product_in_cart_path = (By.XPATH, "//tr[@id='product-2']/td[2]")
    product_count_path = (By.XPATH, "//tr[@id='product-2']/td[4]")
    checkout_path = (By.XPATH, "//a[@class='btn btn-default check_out']")
    checkout_path_visible = (By.XPATH, "(//div[@class='breadcrumbs'])/ol/li[2]")
    login_path = (By.XPATH, "//*[@id='checkoutModal']/div/div/div[2]/p[2]/a")
    #user_login
    login_email_path = (By.XPATH, "(//input[@placeholder='Email Address'])[1]")
    login_password_path = (By.XPATH, "(//input[@placeholder='Password'])[1]")
    login_button = (By.XPATH, "(//button[@data-qa='login-button'])[1]")
    cart_path = (By.XPATH, "(//ul[@class='nav navbar-nav'])/li[3]")

    #user signup
    name_path = (By.XPATH, "//input[@placeholder='Name']")
    email_path= (By.XPATH, "(//input[@name='email'])[2]")
    signup_path = (By.XPATH, "//button[@data-qa='signup-button']")
    password_path = (By.XPATH, "//input[@id='password']")
    first_name_path = (By.XPATH, "//input[@id='first_name']")
    last_name_path = (By.XPATH, "//input[@id='last_name']")
    address_path = (By.XPATH, "//input[@id='address1']")
    state_path = (By.XPATH, "//input[@id='state']")
    city_path = (By.XPATH, "//input[@id='city']")
    zipcode_path = (By.XPATH, "//input[@id='zipcode']")
    mobile_path = (By.XPATH, "//input[@id='mobile_number']")
    create_path = (By.XPATH, "(//button[@class='btn btn-default'])[1]")
    continue_button_path = (By.XPATH, "//a[@data-qa='continue-button']")
    place_order = (By.XPATH, "//a[@class='btn btn-default check_out']")

    #card details
    card_name  = (By.XPATH, "//input[@name='name_on_card']")
    card_number = (By.XPATH," //input[@data-qa='card-number']")
    cvc = (By.XPATH, "//input[@data-qa='cvc']")
    expiry_month_path = (By.XPATH, "//input[@data-qa='expiry-month']")
    expiry_year_path = (By.XPATH, "//input[@data-qa='expiry-year']")
    pay_path = (By.XPATH, "//button[@data-qa='pay-button']")

    order_place_path = (By.XPATH, "//div[@class='col-sm-9 col-sm-offset-1']/p")
 