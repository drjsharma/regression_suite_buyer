import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from setup.creds import EMAIL,PASSWORD,URL

def login(driver):
    """ ✅ Reusable Login Function with Explicit Waits & URL Check """
    driver.get(URL)
    
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    # Wait for email field to be present
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, ":r1:")

    # Enter login credentials
    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)

    # Wait until the login button is clickable, then click
    wait.until(EC.element_to_be_clickable((By.ID, ":r1:"))).click()

    # Wait until URL contains "dashboard" (indicating successful login)
    wait.until(lambda driver: "dashboard" in driver.current_url)

