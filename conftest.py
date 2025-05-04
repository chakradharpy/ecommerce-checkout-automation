import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os

# Ensure the project root is included in the path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

def pytest_addoption(parser):
    parser.addoption("--keep-browser-open", action="store_true", help="Don't close browser after test")

@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    request.cls.driver = driver

    yield  # Run the test

    if not request.config.getoption("--keep-browser-open"):
        driver.quit()
