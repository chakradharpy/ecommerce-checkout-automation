import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    # Headless support for CI/CD
    if os.environ.get("CI") == "true":
        options.add_argument('--headless=new')  # New headless mode for Chrome >= 109
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    request.cls.driver = driver

    yield
    driver.quit()
