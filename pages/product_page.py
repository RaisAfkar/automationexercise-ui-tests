from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage(BasePage):

    PRODUCT_BTN = (By.PARTIAL_LINK_TEXT, "Products")
    PRODUCTS_NAME= (By.CSS_SELECTOR, ".productinfo p")
    PRODUCT_VIEW_PRODUCT = (By.CSS_SELECTOR, "a[href^='/product_details/']")
    PRODUCT_SEARCH = (By.ID, "search_product")
    PRODUCT_SEARCH_BTN = (By.ID, "submit_search")
    PRODUCT_SEARCHED_PRODUCT_HEADER = (By.XPATH, "//h2[text()='Searched Products']")
    PRODUCT_HOVER = (By.CSS_SELECTOR, "img[src^='/get_product_picture/']")
    PRODUCT_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "div.overlay-content a")
    PRODUCT_VIEW_CART_BTN = (By.LINK_TEXT, "View Cart")
    PRODUCT_CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")


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
    
    def hover_product_by_index(self, index=1):
        product = self.find_all(self.PRODUCT_HOVER)
        target_product = product[index - 1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", target_product)
        actions = ActionChains(self.driver)
        actions.move_to_element(target_product).perform()

    def click_add_to_cart_by_index(self, index=1):
        add_to_cart = self.find_all(self.PRODUCT_ADD_TO_CART_BTN)
        add_to_cart[index - 1].click()
    
    def click_continue_button(self):
        self.click(self.PRODUCT_CONTINUE_SHOPPING)
    
    def click_view_cart_button(self):
        self.click(self.PRODUCT_VIEW_CART_BTN)