from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*PPL.ADD_TO_BASKET)
        link.click()
        # self.solve_quiz_and_get_code()

    def test_correct_item_in_basket(self):
        name_basket = self.browser.find_elements(
            *PPL.PRODUCT_NAME_IN_BASKET)[0]
        name_item = self.browser.find_element(*PPL.PRODUCT_NAME)
        assert name_basket.text == name_item.text.strip(), "Different product name!"
        price_basket = self.browser.find_element(
            *PPL.PRODUCT_PRICE_IN_BASKET)
        price_item = self.browser.find_element(*PPL.PRODUCT_PRICE)
        assert price_basket.text == price_item.text, "Different product name!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PPL.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*PPL.SUCCESS_MESSAGE), \
            "Success message should disappear"
