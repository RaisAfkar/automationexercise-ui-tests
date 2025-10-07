from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CreateAccount(BasePage):

    ACCOUNT_TITLE = (By.ID, "id_gender1")
    ACCOUNT_PASSWORD = (By.ID, "password")
    ACCOUNT_BIRTH_DAY = (By.ID, "days")
    ACCOUNT_BIRTH_MONTH = (By.ID, "months")
    ACCOUNT_BIRTH_YEAR = (By.ID, "years")
    ACCOUNT_NEWSLATTER = (By.ID, "newsletter")
    ACCOUNT_FIRSTNAME = (By.NAME, "first_name")
    ACCOUNT_LASTNAME = (By.NAME,"last_name")
    ACCOUNT_ADDRESS = (By.NAME, "address1")
    ACCOUNT_COUNTRY = (By.ID, "country")
    ACCOUNT_STATE = (By.ID, "state")
    ACCOUNT_CITY = (By.ID, "city")
    ACCOUNT_ZIPCODE = (By.ID, "zipcode")
    ACCOUNT_MOBILE_NUMBER = (By.ID, "mobile_number")
    ACCOUNT_BTN_CREATE_ACCOUNT = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED = (By.CSS_SELECTOR, "h2.title")
    ACCOUNT_BTN_CONTINUE = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    ACCOUNT_LOGGED = (By.XPATH, "//ul[@class='nav navbar-nav']//a[contains(text(), 'Logged')]")

    def click_radio_btn(self):
        self.click(self.ACCOUNT_TITLE)
    
    def entered_password(self, password):
        self.type(self.ACCOUNT_PASSWORD, password)
    
    def selected_day_value(self, days):
        self.selected_by_value(self.ACCOUNT_BIRTH_DAY, days)
    
    def selected_month_value(self, month):
        self.selected_by_value(self.ACCOUNT_BIRTH_MONTH, month)
    
    def selected_year_value(self, year):
        self.selected_by_value(self.ACCOUNT_BIRTH_YEAR, year)
    
    def click_checkbox(self):
        self.click(self.ACCOUNT_NEWSLATTER)
    
    def entered_addres_information(self, first, last, address, state, city, zipcode, mobile):
        self.type(self.ACCOUNT_FIRSTNAME, first)
        self.type(self.ACCOUNT_LASTNAME, last)
        self.type(self.ACCOUNT_ADDRESS, address)
        self.type(self.ACCOUNT_STATE, state)
        self.type(self.ACCOUNT_CITY, city)
        self.type(self.ACCOUNT_ZIPCODE, zipcode)
        self.type(self.ACCOUNT_MOBILE_NUMBER, mobile)
    
    def click_btn_create_account(self):
        self.click(self.ACCOUNT_BTN_CREATE_ACCOUNT)
    
    def get_account_created(self):
        return self.get_text(self.ACCOUNT_CREATED)
    
    def click_btn_continue(self):
        self.click(self.ACCOUNT_BTN_CONTINUE)
    
    def get_logged_username(self):
        return self.get_text(self.ACCOUNT_LOGGED)
    
    def get_validate_required_message(self, locator):
        return self.validation_message(locator)
    
