import allure, pytest
from pages.product_detail_page import DetailsProduct
from pages.product_page import ProductPage
from utils.data_save import save_data
from config import BASE_URL

@allure.feature("Product and Detail Product")
class TestProductDetail:

    @pytest.mark.smoke
    @allure.story("Verify all Products and product_detail_page")
    @allure.severity(allure.severity_level.NORMAL)
    def testing_product_detail_product(self, driver):
        product = ProductPage(driver)

        with allure.step("Open Homepage"):
            product.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on Products button"):
            product.click_product_btn()
            assert "products" in driver.current_url
        
        with allure.step("The products list is visible"):
            products_name = product.all_product_is_visible()
            assert all(item.is_displayed() for item in products_name)
        
        with allure.step("Scrape the product name"):
            data = product.scrape_product_name()
            file_path = save_data("scrape_product.csv", data)
            assert len(data) == 34, f"Expected != result, data: {len(data)}"
        
        with allure.step("Click on View Product of first product"):
            product.click_view_product_by_index(1)
            assert "product_details" in driver.current_url
        
        details = DetailsProduct(driver)

        with allure.step("Verify that detail detail is visible: product name, category, price, availability, condition, brand"):
            details_product = details.get_details_product()
            assert details_product["name"], "Product name should not be empty"
            assert "Category" in details_product["category"], "Category should contain 'Category:'"
            assert "Rs." in details_product["price"], "Price should contain currency"
            assert "Availability" in details_product["availability"], "Availability info missing"
            assert "Condition" in details_product["condition"], "Condition info missing"
            assert "Brand" in details_product["brand"], "Brand info missing"
        

        
