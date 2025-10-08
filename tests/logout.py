import allure,pytest
from pages.login_page import LoginPage
from config import BASE_URL
from utils.data_loader import load_data

@allure.feature("Logout")
class TestLogout:

    @pytest.mark.parametrize("user",load_data("logout_data.csv"))
    @pytest.mark.smoke
    @allure.story("Logout user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self,driver,user):
        logout = LoginPage(driver)

        with allure.step("Open Homepage"):
            logout.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on 'Signup / Login' button"):
            logout.click_signup_or_login_button()
            assert "login" in driver.current_url
        
        with allure.step("Verify 'Login to your account' is visible"):
            header = logout.get_login_header_page()
            assert header == "Login to your account", f"Expected != result, header:{header}"
        
        with allure.step(" Enter correct email address and password"):
            logout.fill_login_form(
                user["email"],
                user["password"]
            )
        
        with allure.step("Click login button"):
            logout.click_login_btn()
        
        with allure.step("Verify that Logout is visible"):
            logout_button = logout.logout_button_is_visible()
            assert logout_button.is_displayed(), f"Button logout not found"
        
        with allure.step("Click 'Logout' button and Verify that user is navigated to login page"):
            logout.click_logout_btn()
            assert "login" in driver.current_url