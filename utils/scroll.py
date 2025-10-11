from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time

def scroll_to_element(driver:WebDriver, element:WebElement, align_to_top: bool=True):
    driver.execute_script("arguments[0].scrollIntoView(arguments[1]);", element, align_to_top)
    time.sleep(1)

def scroll_to_bottom(driver:WebDriver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)