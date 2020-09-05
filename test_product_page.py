import pytest
from time import time
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


link_product = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = str(time()) + '@test.com'
        password = '123456qwert'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(sefl, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.add_to_basket()
        page.should_be_correct_item_in_basket()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.add_to_basket()
    page.should_be_correct_item_in_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link_product)
    page.should_not_be_items_in_basket()
    page.should_be_message_empty_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.add_to_basket()
    page.should_dissapear_of_success_message()
