"""
login_page.py — Page Object for the SauceDemo Login page.

URL: https://www.saucedemo.com/
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Represents the SauceDemo login page.
    Contains all locators and actions specific to this page.
    Test files should NEVER contain locators — only use these methods.
    """

    # --- Locators ---
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_CLOSE_BUTTON = (By.CLASS_NAME, "error-button")

    # --- Actions ---

    def open(self):
        """Navigate to the login page."""
        self.navigate_to(self.URL)
        return self

    def enter_username(self, username: str):
        """Type into the username field."""
        self.type_text(self.USERNAME_INPUT, username)
        return self

    def enter_password(self, password: str):
        """Type into the password field."""
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def click_login(self):
        """Click the Sign In button."""
        self.click(self.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str):
        """Perform a full login: enter credentials and submit."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    # --- Assertions / State Queries ---

    def get_error_message(self) -> str:
        """Return the text of the displayed error message."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        """Return True if an error message is visible on the page."""
        return self.is_displayed(self.ERROR_MESSAGE)

    def is_on_login_page(self) -> bool:
        """Return True if the current URL is the login page."""
        return self.URL in self.get_current_url()
