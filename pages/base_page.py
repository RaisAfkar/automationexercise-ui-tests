from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def open(self, url):
        self.driver.get(url)
    
    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def find_all(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def selected_by_value(self, locator, value):
        element = Select(self.wait.until(
            EC.presence_of_element_located(locator)
        ))
        element.select_by_value(value)
    
    def type(self, locator, text):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    def handling_alert(self, accept=True):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return text
    
    def validation_message(self, locator):
        return self.find(locator).get_attribute("validationMessage")
    
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def is_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))