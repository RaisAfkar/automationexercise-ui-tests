import allure,pytest
from config import BASE_URL
from pages.cart_page import CartPage
from pages.product_page import ProductPage

@allure.feature("Add product")
class TestAddProduct:

    @pytest.mark.smoke
    @allure.story("Test Add product and verify product in cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product(self, driver):
        product = ProductPage(driver)
        cart = CartPage(driver)

        with allure.step("Open Homepage"):
            product.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on Products button"):
            product.click_product_btn()
            assert "products" in driver.current_url
        
        with allure.step("Hover over first product"):
            product.hover_product_by_index(1)
        
        with allure.step("click Add to Cart"):
            product.click_add_to_cart_by_index(1)
        
        with allure.step("Click Continue Shopping button"):
            product.click_continue_button()
        
        with allure.step("Hover over second product"):
            product.hover_product_by_index(2)
        
        with allure.step("click Add to Cart"):
            product.click_add_to_cart_by_index(2)
        
        with allure.step("Click View Cart button"):
            product.click_view_cart_button()
            assert "view_cart" in driver.current_url
        
        with allure.step("Verify both products are added to Cart"):
            expected_product_in_cart = ["1","2"]
            actual_product_in_cart = cart.get_cart_product()
            assert expected_product_in_cart == actual_product_in_cart, f"the product in cart should have id: {actual_product_in_cart}, got: {expected_product_in_cart}"
        
        with allure.step("Verify their prices, quantity and total price"):
            expected = {
                "description": ["Blue Top", "Men Tshirt"],
                "price": ["Rs. 500", "Rs. 400"],
                "quantity": ["1", "1"],
                "total": ["Rs. 500", "Rs. 400"] 
            }
            actual = cart.check_product_in_cart()
            assert actual["description"] == expected["description"], f"The Description product sholuld 'Blue Top' and 'Men Tshirt'"
            assert actual["price"] == expected["price"], f"The Price product sholuld 'Rs. 500' and 'Rs. 400'"
            assert actual["quantity"] == expected["quantity"],f"The Price quantity sholuld 1"
            assert actual["total"] == expected["total"], f"The total price product sholuld 'Rs. 500' and 'Rs. 400'"