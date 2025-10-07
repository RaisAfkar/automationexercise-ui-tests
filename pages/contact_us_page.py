from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsPage(BasePage):

    CONTACT_US_BTN = (By.PARTIAL_LINK_TEXT, "Contact")
    CONTACT_HEADER = (By.CSS_SELECTOR,"div.contact-form h2.text-center")
    CONTACT_NAME = (By.NAME, "name")
    CONTACT_EMAIL = (By.NAME, "email")
    CONTACT_SUBJECT = (By.NAME, "subject")
    CONTACT_MESSAGE = (By.ID, "message")
    CONTACT_UPLOAD_FILE = (By.NAME, "upload_file")
    CONTACT_SUBMIT_BTN = (By.NAME, "submit")
    CONTACT_SUCCESS_SUBMIT = (By.CSS_SELECTOR, "div.alert-success")
    CONTACT_HOME_BTN = (By.XPATH, "//a[@class='btn btn-success']")

    def click_contactUs_button(self):
        self.click(self.CONTACT_US_BTN)
    
    def get_header_contactUs_page(self):
        return self.get_text(self.CONTACT_HEADER)
    
    def fill_contactUs_form(self, name, email, subject, message):
        self.type(self.CONTACT_NAME, name)
        self.type(self.CONTACT_EMAIL, email)
        self.type(self.CONTACT_SUBJECT, subject)
        self.type(self.CONTACT_MESSAGE, message)
    
    def uploaded_file(self, file):
        self.type(self.CONTACT_UPLOAD_FILE, file)
    
    def click_submit_button(self):
        self.click(self.CONTACT_SUBMIT_BTN)
    
    def click_oke_alert_button(self):
        self.handling_alert(True)
    
    def get_success_submit(self):
        return self.get_text(self.CONTACT_SUCCESS_SUBMIT)
    
    def click_home_button(self):
        self.click(self.CONTACT_HOME_BTN)
    
    def get_validate_required_field(self):
        return self.validation_message(self.CONTACT_EMAIL)