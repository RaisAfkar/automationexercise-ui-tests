import allure, pytest
from pages.product_page import ProductPage
from utils.data_save import save_data
from utils.data_loader import load_data
from config import BASE_URL

@allure.feature("Search Product")
class TestSearchProduct:

    @pytest.mark.parametrize("product_name", load_data("product_name.json")["product"])
    @pytest.mark.smoke
    @allure.story("Seacrh Product and Verify the products related to search")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_product(self, driver, product_name):
        product = ProductPage(driver)

        with allure.step("Open Homepage"):
            product.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on Products button"):
            product.click_product_btn()
            assert "products" in driver.current_url
        
        with allure.step("Enter product name in search input"):
            product.enter_product_name(product_name["name"])
        
        with allure.step("click search button"):
            product.click_search_button()

        with allure.step("Verify the searched product is displayed"):
            if product_name.get("expected","") == "is displayed":
                with allure.step("Verify SEARCHED PRODUCTS is visible"):
                    header = product.header_is_visible()
                    assert header.is_displayed(), f"Searched product should displayed"
                
                with allure.step("Verify all the products related to search are visible"):
                    searched_products = [item.text for item in product.all_product_is_visible()]
                    assert all("Jeans" in text for text in searched_products), f"Searched product should contain 'jeans'"
                
                with allure.step("Scrape the searched product"):
                    data = product.scrape_product_name()
                    save_data("result_serched_prduct.json", data)
                    assert len(data) == 3, f"the product name contain jeans should total 3"
            
            else:
                with allure.step("Verify the searched product is not displayed"):
                    invisible = product.product_searched_is_invisible()
                    assert invisible, "product searched should is not displayed"
                
                
