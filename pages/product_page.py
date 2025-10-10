from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    PRODUCT_BTN = (By.PARTIAL_LINK_TEXT, "Products")
    PRODUCTS_NAME= (By.CSS_SELECTOR, ".productinfo p")
    PRODUCT_VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href^='/product_details/']")
    PRODUCT_SEARCH = (By.ID, "search_product")
    PRODUCT_SEARCH_BTN = (By.ID, "submit_search")
    PRODUCT_SEARCHED_PRODUCT_HEADER = (By.XPATH, "//h2[text()='Searched Products']")

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
    
    def enter_product_name(self, value):
        self.type(self.PRODUCT_SEARCH, value)
    
    def click_search_button(self):
        self.click(self.PRODUCT_SEARCH_BTN)
    
    def header_is_visible(self):
        return self.is_visible(self.PRODUCT_SEARCHED_PRODUCT_HEADER)
    
    def product_searched_is_invisible(self):
        return self.is_invisible(self.PRODUCTS_NAME)