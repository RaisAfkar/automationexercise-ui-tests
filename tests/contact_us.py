import allure, pytest
from config import BASE_URL
from utils.data_save import save_data
from utils.data_loader import load_data
from pages.contact_us_page import ContactUsPage

@allure.feature("ContactUS")
class TestContactUs:

    @pytest.mark.parametrize("contact_data", load_data("contact_data.csv"))
    @pytest.mark.smoke
    @allure.story("Testing Contact Us Form")
    @allure.severity(allure.severity_level.NORMAL)
    def testing_contactUs_form(self, driver, contact_data):
        file_upload = save_data("contactUs_data.txt", "This is the dummy data for testing upload file")
        contact = ContactUsPage(driver)

        with allure.step("Open Homepage"):
            contact.open(BASE_URL)
            assert "home" in driver.page_source
        
        with allure.step("Click on Contact Us button"):
            contact.click_contactUs_button()
            assert "contact_us" in driver.current_url
        
        with allure.step("Verify GET IN TOUCH is visible"):
            header = contact.get_header_contactUs_page()
            assert header == "GET IN TOUCH", f"Expected != result, header: {header}"
        
        with allure.step("Enter name, email, subject and message"):
            contact.fill_contactUs_form(
                contact_data["name"],
                contact_data["email"],
                contact_data["subject"],
                contact_data["message"]
            )
        
        with allure.step("Upload file"):
            contact.uploaded_file(str(file_upload))
        
        with allure.step("Click Submit button"):
            contact.click_submit_button()
        
        with allure.step("Validate required field"):
            if contact_data.get("expected","").lower() == "true":
                with allure.step("Click Ok button from allert"):
                    contact.click_oke_alert_button()
                
                with allure.step("Verify success message 'Success! Your details have been submitted successfully.' is visible"):
                    succes_message = contact.get_success_submit()
                    assert succes_message == "Success! Your details have been submitted successfully.", f"Expected != result, succes_messge:{succes_message}"
                
                with allure.step("Click 'Home' button and verify that landed to home page successfully"):
                    contact.click_home_button()
                    assert "home" in driver.page_source
                
            else:
                if contact_data["email"] == "user1@.com":
                    with allure.step(f"Check Validation Message {contact.CONTACT_EMAIL}"):
                        msg = contact.get_validate_required_field()
                        allure.attach(
                            body=msg,
                            name = f"Validation Message for the value in email field == user1@.com",
                            attachment_type= allure.attachment_type.TEXT
                        )
                
                elif contact_data["email"] == "user1":
                    with allure.step(f"Check Validation Message {contact.CONTACT_EMAIL}"):
                        msg = contact.get_validate_required_field()
                        allure.attach(
                            body=msg,
                            name = f"Validation Message for the value in email field == user1",
                            attachment_type= allure.attachment_type.TEXT
                        )
                
                elif contact_data["email"] == "":
                    with allure.step(f"Check Validation Message {contact.CONTACT_EMAIL}"):
                        msg = contact.get_validate_required_field()
                        allure.attach(
                            body=msg,
                            name = f"Validation Message for the value in email field == user1",
                            attachment_type= allure.attachment_type.TEXT
                        )

        
