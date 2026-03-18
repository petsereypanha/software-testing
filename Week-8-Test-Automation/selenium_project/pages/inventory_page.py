"""
inventory_page.py — Page Object for the SauceDemo Inventory (Products) page.

URL: https://www.saucedemo.com/inventory.html
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Represents the SauceDemo inventory/products page.
    Accessible only after successful login.
    """

    URL_PATH = "/inventory.html"

    # --- Locators ---
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # --- Actions ---

    def get_page_heading(self) -> str:
        """Return the 'Products' heading text."""
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self) -> int:
        """Return the number of products displayed on the page."""
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_product_names(self) -> list:
        """Return a list of all product names displayed."""
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def get_product_prices(self) -> list:
        """Return a list of all product prices as floats."""
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]

    def add_first_item_to_cart(self):
        """Click 'Add to Cart' for the first product in the list."""
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if buttons:
            buttons[0].click()
        return self

    def get_cart_item_count(self) -> int:
        """Return the number shown on the cart badge. Returns 0 if badge not visible."""
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0

    def go_to_cart(self):
        """Click the shopping cart icon to go to the cart page."""
        self.click(self.CART_LINK)

    def sort_products(self, sort_option: str):
        """
        Sort products using the dropdown.
        sort_option values: 'az', 'za', 'lohi', 'hilo'
        """
        select = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        select.select_by_value(sort_option)
        return self

    def logout(self):
        """Open burger menu and click logout."""
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)

    def is_on_inventory_page(self) -> bool:
        """Return True if currently on the inventory page."""
        return self.URL_PATH in self.get_current_url()
