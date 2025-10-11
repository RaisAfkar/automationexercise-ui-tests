from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.scroll import scroll_to_element

class HomePage(BasePage):

    HOME_FIND_PRODUCT = (By.CSS_SELECTOR, "img[src^='/get_product_picture/']")
    HOME_VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href^='/product_details/']")

    def scroll_to_desired_product(self, index=1):
        product = self.find_all(self.HOME_FIND_PRODUCT)
        desired_product = product[index - 1]
        scroll_to_element(self.driver, desired_product)
        
    def click_view_product_by_index(self, index=1):
        element = self.find_all(self.HOME_VIEW_PRODUCT)
        element[index - 1].click()