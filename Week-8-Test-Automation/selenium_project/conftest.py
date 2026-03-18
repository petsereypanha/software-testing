"""
conftest.py — Shared pytest fixtures for the Selenium test suite.

Fixtures defined here are automatically available to all test files
without needing to import them explicitly.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


BASE_URL = "https://www.saucedemo.com"

VALID_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def driver():
    """
    Provide a Chrome WebDriver instance for each test function.
    Automatically quits the browser after each test (even if the test fails).
    scope="function" means a fresh browser is opened for every single test.
    """
    options = Options()
    # Uncomment the line below to run tests headlessly (no browser window)
    # options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Selenium >= 4.6 manages ChromeDriver automatically
    d = webdriver.Chrome(options=options)
    d.implicitly_wait(5)  # Fallback implicit wait — prefer explicit waits in tests
    yield d
    d.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Provides a driver that is already logged in with the standard user.
    Use this fixture in tests that require authentication but are NOT
    testing the login flow itself.
    """
    driver.get(BASE_URL)
    driver.find_element("id", "user-name").send_keys(VALID_USER)
    driver.find_element("id", "password").send_keys(PASSWORD)
    driver.find_element("id", "login-button").click()
    yield driver
