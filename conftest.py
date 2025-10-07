import allure, pytest, json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver(request):
    options = Options()
    options.add_argument("--start-maximized")
    options.set_capability("goog:loggingPrefs",{"performance":"ALL"})
    driver = webdriver.Chrome(
        options = options,
        service= Service(ChromeDriverManager().install())
    )
    yield driver

    try:
        screenshoot = driver.get_screenshot_as_png()
        allure.attach(
            screenshoot,
            name = f"{request.node.name}_screenshoot",
            attachment_type = allure.attachment_type.PNG
        )
    except Exception as e:
        allure.attach(
            str(e),
            name = f"screenshoot_error",
            attachment_type = allure.attachment_type.TEXT
        )
    
    try:
        perf_log = driver.get_log("performance")
        if perf_log:
            log_json = json.dumps(perf_log, indent=2)
            allure.attach(
                log_json,
                name = f"{request.node.name}_network",
                attachment_type= allure.attachment_type.JSON
            )
    except Exception as e:
        allure.attach(
            str(e),
            name = f"network_error",
            attachment_type = allure.attachment_type.TEXT
        )
    
    driver.quit()