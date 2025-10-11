from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CART_PRODUCT = (By.CSS_SELECTOR,"tr[id^='product-']")
    CART_ITEM = (By.XPATH, "//td[@class='cart_product']//img[src^='get_product_picture/']")
    CART_DESCRIPTION = (By.XPATH, "//td[@class='cart_description']//a") 
    CART_PRICE = (By.XPATH, "//td[@class='cart_price']")
    CART_QUANTITY = (By.XPATH, "//td[@class='cart_quantity']")
    CART_TOTAL = (By.XPATH, "//td[@class='cart_total']")
    CART_DELETE_ITEM = (By.XPATH, "//td[@class='cart_delete']//a")
    CART_CHECKOUT_BTN = (By.XPATH, "a[text()='Proceed To Checkout']")

    def get_cart_product(self):
        products = self.find_all(self.CART_PRODUCT)
        return [p.get_attribute("id").replace("product-","") for p in products]

    def check_product_in_cart(self):
        description = [d.text for d in self.find_all(self.CART_DESCRIPTION)]
        price = [p.text for p in self.find_all(self.CART_PRICE)]
        quantity = [q.text for q in self.find_all(self.CART_QUANTITY)]
        total = [t.text for t in self.find_all(self.CART_TOTAL)]
        return {
            "description": description,
            "price": price,
            "quantity": quantity,
            "total": total
        }
    