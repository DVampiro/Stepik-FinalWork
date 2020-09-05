from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "btn-block")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators ():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
