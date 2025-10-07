from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUpPage(BasePage):

    SIGNUP_OR_LOGIN_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    SIGNUP_HEADER = (By.CSS_SELECTOR, "div.signup-form h2")
    SIGNUP_NAME = (By.NAME, "name")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BTN = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    SIGNUP_ERROR_TEXT = (By.XPATH, "//p[contains(text(), 'Email')]")
    SIGNUP_SUCCES = (By.TAG_NAME, "label")

    def click_signup_or_login_button(self):
        self.click(self.SIGNUP_OR_LOGIN_BTN)
    
    def get_header_text(self):
        return self.get_text(self.SIGNUP_HEADER)
    
    def fill_form_signup(self, name, email):
        self.type(self.SIGNUP_NAME, name)
        self.type(self.SIGNUP_EMAIL, email)

    def click_btn_signup(self):
        self.click(self.SIGNUP_BTN)

    def get_error_text(self):
        return self.get_text(self.SIGNUP_ERROR_TEXT)
    
    def check_succes_register(self):
        return self.is_visible(self.SIGNUP_SUCCES)
    
    def get_validate_required_message(self, locator):
        self.validation_message(locator)