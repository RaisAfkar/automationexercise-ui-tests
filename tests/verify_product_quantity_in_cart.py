import allure,pytest,time
from config import BASE_URL
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_detail_page import DetailsProduct

@allure.feature("Cart Page")
class TestQuantityInCart:

    @allure.story("Increase quantity and add to cart")
    @allure.title("Verify Product quantity in Cart")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verifiy_quantity(self, driver):
        home = HomePage(driver)
        detail = DetailsProduct(driver)
        cart = CartPage(driver)

        with allure.step("Open Homepage"):
            home.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Find the product to be purchased on home page"):
            home.scroll_to_desired_product(30)
        
        with allure.step("Click View Product for any product on home page"):
            home.click_view_product_by_index(30)
            assert "product_details" in driver.current_url
        
        with allure.step("Increase quantity to 4"):
            detail.input_quantity("4")
        
        with allure.step("Click Add to cart button"):
            detail.click_add_to_cart_button()
        
        with allure.step("Click View Cart button"):
            detail.click_view_cart_btn()
            time.sleep(3)
        
        with allure.step("Verify that product is displayed in cart page with exact quantity"):
            expected = {
                "quantity" : ["4"]
            }

            actual = cart.check_product_in_cart()
            assert actual["quantity"] == expected["quantity"], "quantity product should 4"
        
