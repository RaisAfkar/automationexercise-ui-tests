from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    PRODUCT_BTN = (By.PARTIAL_LINK_TEXT, "Products")
    PRODUCTS_NAME= (By.CSS_SELECTOR, ".productinfo p")
    PRODUCT_VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href^='/product_details/']")

    def click_product_btn(self):
        self.click(self.PRODUCT_BTN)
    
    def all_product_is_visible(self):
        return self.find_all(self.PRODUCTS_NAME)

    def scrape_product_name(self):
        element = self.find_all(self.PRODUCTS_NAME)
        data = [
            {"no": index,"product_name": product.text.strip()}
            for index,product in enumerate(element, start=1)
        ]
        return data

    def click_view_product_by_index(self, index=1):
        element = self.find_all(self.PRODUCT_VIEW_PRODUCT)
        element[index - 1].click()