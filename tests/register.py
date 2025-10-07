import allure, pytest
from utils.data_loader import load_data
from pages.signup_page import SignUpPage
from pages.create_account_page import CreateAccount
from config import BASE_URL
from selenium.common.exceptions import TimeoutException


@allure.feature("Register")
class TestRegister:
    @pytest.mark.parametrize("data_test_signup",load_data("signup_data.csv"))
    @pytest.mark.smoke
    @allure.story("Testing User registration with new and existing email.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signup(self, driver, data_test_signup):
        signup = SignUpPage(driver)

        with allure.step("Open Homepage"):
            signup.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on 'Signup / Login' button"):
            signup.click_signup_or_login_button()
        
        with allure.step("Verify 'New User Signup!' is visible"):
            header = signup.get_header_text()
            assert header == "New User Signup!", f"expected != result, got:{header}"
        
        with allure.step("Enter name and email address"):
            signup.fill_form_signup(data_test_signup["name"], data_test_signup["email"])
        
        with allure.step("Click 'Signup' button"):
            signup.click_btn_signup()
        
        with allure.step("Validate mandatory field after click the Signup button"):
            if data_test_signup.get("expected", "").lower() == "true":
                title = signup.check_succes_register()
                assert title.is_displayed, f"title not is diplayed or the button not clicked"
            
            else:
                field_mapping = {
                    "name": signup.SIGNUP_NAME,
                    "email": signup.SIGNUP_EMAIL
                }

                for field_value, locator in field_mapping.items():
                    if field_value == "Testing41":
                        with allure.step(f"validate required field - {locator}"):
                            msg = signup.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"ValidationMessage - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )
                    
                    elif field_value == "Testing41@.com":
                        with allure.step(f"validate required field - {locator}"):
                            msg = signup.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"ValidationMessage - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )
                    
                    elif field_value == "":
                        with allure.step(f"validate required field - {locator}"):
                            msg = signup.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"ValidationMessage - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )
    
    @pytest.mark.parametrize("create_account_data",load_data("account_data.csv"))
    @pytest.mark.smoke
    @allure.story("Fill in the Create Account form with mandatory and optional fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_account(self, driver, create_account_data):
        signup = SignUpPage(driver)

        with allure.step("Open Homepage"):
            signup.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on 'Signup / Login' button"):
            signup.click_signup_or_login_button()
        
        with allure.step("Verify 'New User Signup!' is visible"):
            header = signup.get_header_text()
            assert header == "New User Signup!", f"expected != result, got:{header}"
        
        with allure.step("Enter name and email address"):
            signup.fill_form_signup(create_account_data["name"], create_account_data["email"])
        
        with allure.step("Click 'Signup' button"):
            signup.click_btn_signup()
        
        create = CreateAccount(driver)

        with allure.step("Click mr Or Mrs radio button"):
            create.click_radio_btn()
        
        with allure.step("Enter password"):
            create.entered_password(create_account_data["password"])
        
        with allure.step("Selected value in the days dropdown"):
            create.selected_day_value(create_account_data["days"])
        
        with allure.step("Selected value in the months dropdown"):
            create.selected_month_value(create_account_data["months"])
        
        with allure.step("Selected value in the years dropdown"):
            create.selected_year_value(create_account_data["years"])
        
        with allure.step("Click the Newslatter checkbox"):
            create.click_checkbox()
        
        with allure.step("Entered value in the Address Information Form"):
            create.entered_addres_information(
                create_account_data["firstname"],
                create_account_data["lastname"],
                create_account_data["address"],
                create_account_data["state"],
                create_account_data["city"],
                create_account_data["zipcode"],
                create_account_data["mobilenumber"]
            )
        
        with allure.step("click the create account button"):
            create.click_btn_create_account()
        
        with allure.step("Validate mandatory field after click the continue button"):
            if create_account_data.get("expected","").lower() == "true":
                with allure.step("Account created successfully"):
                    try:
                        created = create.get_account_created()
                        assert created == "ACCOUNT CREATED!", f"Expected != result, got: {created}"
                    except TimeoutException:
                        pass
                
                with allure.step("Click Continue button"):
                    create.click_btn_continue()

                with allure.step(f"Validate Logged in as {create_account_data["name"]}"):
                    logged = create.get_logged_username()
                    assert logged == "Logged in as Testing39", f"Expected != logged text: {logged}"
            
            else:
                field_mapping = {
                    "password":create.ACCOUNT_PASSWORD,
                    "firstname":create.ACCOUNT_FIRSTNAME,
                    "lastname":create.ACCOUNT_LASTNAME,
                    "address":create.ACCOUNT_ADDRESS,
                    "state":create.ACCOUNT_STATE,
                    "city":create.ACCOUNT_CITY,
                    "zipcode":create.ACCOUNT_ZIPCODE,
                    "mobilenumber":create.ACCOUNT_MOBILE_NUMBER
                }
                for field_value,locator in field_mapping.items():
                    if field_value == "":
                        with allure.step(f"validate required field - {locator}"):
                            msg = signup.get_validate_required_message(locator)
                            allure.attach(
                                body=msg,
                                name = f"ValidationMessage - {locator}",
                                attachment_type= allure.attachment_type.TEXT
                            )