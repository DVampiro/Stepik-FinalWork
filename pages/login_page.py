from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        textbox_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        textbox_email.send_keys(email)
        textbox_password1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS1)
        textbox_password1.send_keys(password)
        textbox_password2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS2)
        textbox_password2.send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.BUTTON_REGISTRATION).click()

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Not login page"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"
