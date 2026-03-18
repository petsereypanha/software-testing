"""
test_login.py — Test cases for the SauceDemo login functionality.

Covers:
- TC_LOGIN_001: Successful login with valid credentials
- TC_LOGIN_002: Login fails with incorrect password
- TC_LOGIN_003: Login fails with incorrect username
- TC_LOGIN_004: Login fails with empty username
- TC_LOGIN_005: Login fails with empty password
- TC_LOGIN_006: Login fails with empty username AND password
- TC_LOGIN_007: Locked-out user receives appropriate message
- TC_LOGIN_008: Parametrized invalid login scenarios
- TC_LOGIN_009: Successful logout after login
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from conftest import VALID_USER, LOCKED_USER, PASSWORD


class TestLogin:
    """Test cases for the login functionality."""

    def test_TC_LOGIN_001_successful_login(self, driver):
        """Valid user should be redirected to the inventory page after login."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_on_inventory_page(), \
            f"Expected to be on inventory page, but URL was: {driver.current_url}"
        assert inventory_page.get_page_heading() == "Products"

    def test_TC_LOGIN_002_wrong_password(self, driver):
        """Login with correct username but wrong password should show an error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, "wrongpassword123")

        assert login_page.is_error_displayed(), "Error message should be visible"
        assert "Username and password do not match" in login_page.get_error_message()
        assert login_page.is_on_login_page(), "User should remain on login page"

    def test_TC_LOGIN_003_wrong_username(self, driver):
        """Login with incorrect username should show an error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("nonexistent_user", PASSWORD)

        assert login_page.is_error_displayed(), "Error message should be visible"

    def test_TC_LOGIN_004_empty_username(self, driver):
        """Submitting login with empty username should show a validation error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", PASSWORD)

        assert login_page.is_error_displayed()
        assert "Username is required" in login_page.get_error_message()

    def test_TC_LOGIN_005_empty_password(self, driver):
        """Submitting login with empty password should show a validation error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, "")

        assert login_page.is_error_displayed()
        assert "Password is required" in login_page.get_error_message()

    def test_TC_LOGIN_006_both_fields_empty(self, driver):
        """Submitting login with both fields empty should show username required error."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("", "")

        assert login_page.is_error_displayed()
        assert "Username is required" in login_page.get_error_message()

    def test_TC_LOGIN_007_locked_out_user(self, driver):
        """Locked out user should see descriptive locked-out error message."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(LOCKED_USER, PASSWORD)

        assert login_page.is_error_displayed()
        assert "locked out" in login_page.get_error_message().lower()

    @pytest.mark.parametrize("username,password,expected_error_fragment", [
        ("wrong_user", "wrong_pass", "do not match"),
        ("standard_user", "wrong_pass", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ])
    def test_TC_LOGIN_008_invalid_login_scenarios(self, driver, username, password, expected_error_fragment):
        """Multiple invalid login combinations should all show appropriate errors."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)

        assert login_page.is_error_displayed(), \
            f"Expected error for user='{username}', pass='{password}'"
        assert expected_error_fragment in login_page.get_error_message(), \
            f"Error message '{login_page.get_error_message()}' should contain '{expected_error_fragment}'"

    def test_TC_LOGIN_009_logout(self, logged_in_driver):
        """User should be able to log out and be returned to login page."""
        inventory_page = InventoryPage(logged_in_driver)
        assert inventory_page.is_on_inventory_page()

        inventory_page.logout()

        login_page = LoginPage(logged_in_driver)
        assert login_page.is_on_login_page(), "After logout, user should be on login page"
