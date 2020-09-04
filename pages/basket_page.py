from .base_page import BasePage
from .locators import BasketPageLocators as BPL


class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.find_count_elements(
            *BPL.EMPTY_MESSAGE) == 1, 'Not find empty message'

    def should_not_be_items_in_basket(self):
        assert self.is_disappeared(*BPL.CHECKOUT_BUTTON), \
            "Basket is not empty"
