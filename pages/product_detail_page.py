from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DetailsProduct(BasePage):

    DETAIL_PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    DETAIL_PRODUCT_CATEGORY = (By.CSS_SELECTOR, ".product-information p")
    DETAIL_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-information span span")
    DETAIL_PRODUCT_AVAILABILITY = (By.XPATH, "//p[contains(text(), 'In')]")
    DETAIL_PRODUCT_CONDITION = (By.XPATH, "//p[contains(text(), 'New')]")
    DETAIL_PRODUCT_BRAND = (By.XPATH, "//p[contains(text(), 'Polo')]")

    def get_details_product(self):
        return {
            "name" : self.get_text(self.DETAIL_PRODUCT_NAME),
            "category" : self.get_text(self.DETAIL_PRODUCT_CATEGORY),
            "price" : self.get_text(self.DETAIL_PRODUCT_PRICE),
            "availability" : self.get_text(self.DETAIL_PRODUCT_AVAILABILITY),
            "condition" : self.get_text(self.DETAIL_PRODUCT_CONDITION),
            "brand" : self.get_text(self.DETAIL_PRODUCT_BRAND)
        }