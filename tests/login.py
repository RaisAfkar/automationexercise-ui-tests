import allure, pytest
from pages.login_page import LoginPage
from utils.data_loader import load_data
from config import BASE_URL

@allure.feature("Login")
class TestLogin:

    @pytest.mark.parametrize("login_data", load_data("login_data.csv"))
    @pytest.mark.smoke
    @allure.story("Login user with correct and incorrect email and password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, driver, login_data):
        login = LoginPage(driver)

        with allure.step("Open Homepage"):
            login.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on 'Signup / Login' button"):
            login.click_signup_or_login_button()
            assert "login" in driver.current_url
        
        with allure.step("Verify 'Login to your account' is visible"):
            header = login.get_login_header_page()
            assert header == "Login to your account", f"Expected != result, header:{header}"
        
        with allure.step("Enter email address and password"):
            login.fill_login_form(
                login_data["email"],
                login_data["password"]
            )
        
        with allure.step("Click login button"):
            login.click_login_btn()
        
        with allure.step("Validate required field after click the login button"):
            if login_data.get("expected","").lower() == "true":
                with allure.step(f"Verify that Logged in as username is visible"):
                    username = login.success_login()
                    assert "Testing78" in username, f"Expected != result, username: {username}"
            
            else:
                field_mapping = {
                    "email" : login.LOGIN_EMAIL,
                    "password" : login.LOGIN_PASSWORD
                }
                for field_value, locator in field_mapping.items():
                    if field_value == "Testing34@mail.com":
                        with allure.step("Validate the error message is displayed"):
                            error = login.get_login_error()
                            assert error == "Your email or password is incorrect!", f"Expected != result, error: {error}"

                    elif field_value == "Testing33@.com":
                        with allure.step(f"Validate required field - {locator}"):
                            msg = login.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"validate message - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )
                    
                    elif field_value == "Testing33":
                        with allure.step(f"Validate required field - {locator}"):
                            msg = login.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"validate message - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )

                    elif field_value == "":
                        with allure.step(f"Validate required field - {locator}"):
                            msg = login.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"validate message - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )



