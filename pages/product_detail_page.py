from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DetailsProduct(BasePage):

    DETAIL_PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    DETAIL_PRODUCT_CATEGORY = (By.CSS_SELECTOR, ".product-information p")
    DETAIL_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    DETAIL_PRODUCT_AVAILABILITY = (By.XPATH, "//p[contains(text(), 'In')]")
    DETAIL_PRODUCT_CONDITION = (By.XPATH, "//p[contains(text(), 'New')]")
    DETAIL_PRODUCT_BRAND = (By.XPATH, "//p[contains(text(), 'Polo')]")
    DETAIL_INPUT_QUANTITY = (By.ID, "quantity")
    DETAIL_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-default")
    DETAIL_VIEW_CART_BTN = (By.LINK_TEXT, "View Cart")

    def get_details_product(self):
        return {
            "name" : self.get_text(self.DETAIL_PRODUCT_NAME),
            "category" : self.get_text(self.DETAIL_PRODUCT_CATEGORY),
            "price" : self.get_text(self.DETAIL_PRODUCT_PRICE),
            "availability" : self.get_text(self.DETAIL_PRODUCT_AVAILABILITY),
            "condition" : self.get_text(self.DETAIL_PRODUCT_CONDITION),
            "brand" : self.get_text(self.DETAIL_PRODUCT_BRAND)
        }
    
    def input_quantity(self, quantity):
        self.type(self.DETAIL_INPUT_QUANTITY, quantity)
    
    def click_add_to_cart_button(self):
        self.click(self.DETAIL_ADD_TO_CART_BTN)
    
    def click_view_cart_btn(self):
        self.click(self.DETAIL_VIEW_CART_BTN)
    
    
