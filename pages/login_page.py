from .base_page import BasePage
from .locators import LoginPageLocators as LPL


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LPL.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_pass = self.browser.find_element(*LPL.REGISTER_PASS1)
        reg_pass.send_keys(password)
        reg_pass = self.browser.find_element(*LPL.REGISTER_PASS2)
        reg_pass.send_keys(password)
        reg_pass = self.browser.find_element(*LPL.BUTTON_REGISTRATION).click()
