# Framework Used

1. Selenium (WebDriver): Browser automation

2. Pytest: Test framework

3. POM (Page Object Model): For scalable, readable code

4. pytest-html: For beautiful test reports

5. Set python path
set PYTHONPATH=%cd%


# Clone the repository:

git clone https://github.com/chakradharpy/ecommerce-checkout-automation.git
cd ecommerce-checkout-automation

# Install dependencies

pip install -r requirements.txt


# Run all tests with HTML report:
Run all tests with HTML report:


# QA Automation Task with Selenium and Pytest

##  Virtual Environment Setup (Recommended)


# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# run with report in html form
pytest -v --html=report.html --self-contained-html

