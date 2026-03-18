"""
test_inventory.py — Test cases for the SauceDemo inventory (products) page.

Covers:
- TC_INV_001: Products page loads with correct title
- TC_INV_002: At least 6 products are displayed
- TC_INV_003: Adding item to cart updates cart badge
- TC_INV_004: Sort products A to Z
- TC_INV_005: Sort products Z to A
- TC_INV_006: Sort products by price low to high
- TC_INV_007: Sort products by price high to low
"""

import pytest
from pages.inventory_page import InventoryPage


class TestInventory:
    """Test cases for the Products/Inventory page."""

    def test_TC_INV_001_products_page_title(self, logged_in_driver):
        """Inventory page should display 'Products' as the page heading."""
        inventory_page = InventoryPage(logged_in_driver)
        assert inventory_page.get_page_heading() == "Products"

    def test_TC_INV_002_products_count(self, logged_in_driver):
        """At least 6 products should be displayed on the inventory page."""
        inventory_page = InventoryPage(logged_in_driver)
        count = inventory_page.get_product_count()
        assert count >= 6, f"Expected at least 6 products, found {count}"

    def test_TC_INV_003_add_to_cart_updates_badge(self, logged_in_driver):
        """Adding one item to cart should show badge count of 1."""
        inventory_page = InventoryPage(logged_in_driver)

        initial_count = inventory_page.get_cart_item_count()
        assert initial_count == 0, "Cart should start empty"

        inventory_page.add_first_item_to_cart()

        new_count = inventory_page.get_cart_item_count()
        assert new_count == 1, f"Expected cart count of 1, got {new_count}"

    def test_TC_INV_004_sort_a_to_z(self, logged_in_driver):
        """Sorting A-Z should display product names in ascending alphabetical order."""
        inventory_page = InventoryPage(logged_in_driver)
        inventory_page.sort_products("az")

        names = inventory_page.get_product_names()
        assert names == sorted(names), \
            f"Products should be sorted A-Z. Got: {names}"

    def test_TC_INV_005_sort_z_to_a(self, logged_in_driver):
        """Sorting Z-A should display product names in descending alphabetical order."""
        inventory_page = InventoryPage(logged_in_driver)
        inventory_page.sort_products("za")

        names = inventory_page.get_product_names()
        assert names == sorted(names, reverse=True), \
            f"Products should be sorted Z-A. Got: {names}"

    def test_TC_INV_006_sort_price_low_to_high(self, logged_in_driver):
        """Sorting price low-to-high should display cheapest product first."""
        inventory_page = InventoryPage(logged_in_driver)
        inventory_page.sort_products("lohi")

        prices = inventory_page.get_product_prices()
        assert prices == sorted(prices), \
            f"Prices should be sorted low to high. Got: {prices}"

    def test_TC_INV_007_sort_price_high_to_low(self, logged_in_driver):
        """Sorting price high-to-low should display most expensive product first."""
        inventory_page = InventoryPage(logged_in_driver)
        inventory_page.sort_products("hilo")

        prices = inventory_page.get_product_prices()
        assert prices == sorted(prices, reverse=True), \
            f"Prices should be sorted high to low. Got: {prices}"
