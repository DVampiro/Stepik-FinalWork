from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.find_count_elements(
            *BasketPageLocators.EMPTY_MESSAGE) == 1, 'Not find empty message'

    def should_not_be_items_in_basket(self):
        assert self.is_disappeared(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Basket is not empty"
