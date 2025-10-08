from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    SIGNUP_OR_LOGIN_BTN = (By.CSS_SELECTOR, "a[href='/login']")
    LOGIN_HEADER = (By.CSS_SELECTOR, "div.login-form h2")
    LOGIN_EMAIL = (By.NAME, "email")
    LOGIN_PASSWORD = (By.NAME, "password")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(), 'email')]")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_LOGGGED = (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(), 'Logged')]")
    LOGIN_LOGOUT_BUTTON = (By.PARTIAL_LINK_TEXT, "Logout")

    def click_signup_or_login_button(self):
        self.click(self.SIGNUP_OR_LOGIN_BTN)
    
    def get_login_header_page(self):
        return self.get_text(self.LOGIN_HEADER)
    
    def fill_login_form(self, email, password):
        self.type(self.LOGIN_EMAIL, email)
        self.type(self.LOGIN_PASSWORD, password)
    
    def click_login_btn(self):
        self.click(self.LOGIN_BTN)
    
    def success_login(self):
        return self.get_text(self.LOGIN_LOGGGED)

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERROR)
    
    def get_validate_required_message(self, locator):
        self.validation_message(locator)
    
    def logout_button_is_visible(self):
        return self.is_visible(self.LOGIN_LOGOUT_BUTTON)
    
    def click_logout_btn(self):
        self.click(self.LOGIN_LOGOUT_BUTTON)
