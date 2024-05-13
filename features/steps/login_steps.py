from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to initialize the driver
def initialize_driver(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Function to perform login
def login(context, email, password):
    driver = context.driver
    driver.get("your website's login page")  # your website
    
    """ Login Form """
    
    # get element for entering email through XPATH
    get_email = driver.find_element(By.XPATH, 'xpath of email input')
    get_email.send_keys(email)
    # get element for entering password through XPATH
    get_passwd = driver.find_element(By.XPATH, 'xpath of password input')
    get_passwd.send_keys(password)
    
    # get and click login button through XPATH
    driver.find_element(By.XPATH, 'login button xpath').click()
    sleep(4)

# Step definitions
@given('the user is on the login page')
def step_user_on_login_page(context):
    initialize_driver(context)

@when('the user enters valid email and password')
def step_user_enters_valid_credentials(context):
    login(context, "your email", "your password")

@when('clicks on the login button')
def step_user_clicks_login_button(context):
    pass  # The login function already handles clicking the login button

@then('a home page is shown')
def step_home_page_is_shown(context):
    home=context.driver.find_element(By.CLASS_NAME,"for validation")

    assert home is not None



@when('the user enters invalid email or password')
def step_user_enters_valid_credentials(context):
    login(context, "ramroxa@ramro.com", "wrrq")


@then("an error message should be displayed")
def check_err(context):
    err_msg=context.driver.find_element(By.XPATH,'error message xpath')
    assert err_msg is not None


