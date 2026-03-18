"""
base_page.py — Base class for all page objects.

All page classes inherit from BasePage to get common browser interaction
methods. This avoids repeating boilerplate code in every page class.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Base class that all page objects inherit from."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url: str):
        """Navigate to a URL."""
        self.driver.get(url)

    def find(self, locator: tuple):
        """Find a single element with explicit wait for visibility."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: tuple):
        """Find an element and wait until it is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator: tuple):
        """Wait for element to be clickable, then click it."""
        self.find_clickable(locator).click()

    def type_text(self, locator: tuple, text: str):
        """Clear a field and type text into it."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """Return the visible text of an element."""
        return self.find(locator).text

    def is_displayed(self, locator: tuple) -> bool:
        """Return True if element is visible, False if not found/hidden."""
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_url_contains(self, partial_url: str):
        """Wait until the current URL contains the given string."""
        self.wait.until(EC.url_contains(partial_url))

    def get_current_url(self) -> str:
        """Return the current page URL."""
        return self.driver.current_url

    def get_page_title(self) -> str:
        """Return the browser page title."""
        return self.driver.title
