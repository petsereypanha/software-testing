"""
__init__.py — Makes the pages/ directory a Python package.
Import page objects from here for cleaner imports in test files.
"""

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
