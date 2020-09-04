import pytest
from pages.product_page import ProductPage


@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
  page = ProductPage(browser, link)
  page.open()
  page.add_to_basket()
  page.test_correct_item_in_basket()


pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
  page = ProductPage(browser, link)
  page.open()
  page.add_to_basket()
  page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
  page = ProductPage(browser, link)
  page.open()
  page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
  page = ProductPage(browser, link)
  page.open()
  page.add_to_basket()
  page.should_dissapear_of_success_message()
