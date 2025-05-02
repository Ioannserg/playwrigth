from bage_page import BasePage
from playwright.sync_api import sync_playwright, expect

class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR = '.inventory_item:has-text("Sauce Labs Backpack") >> button:has-text("Add to cart")'
    SHOPPING_CART_LINK_SELECTOR = '.shopping_cart_link'
    SHOPPING_CART_SELECTOR = "#shopping_cart_container"
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR)
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.assert_text_in_element(self.SHOPPING_CART_LINK_SELECTOR, '1')
        self.wait_for_selector_and_click(self.SHOPPING_CART_SELECTOR)

