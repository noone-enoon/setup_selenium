from selenium import webdriver
import pytest

DRIVER = "C:\drivers_automation"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.1.4:8081/")
    parser.addoption("--executor", default="192.168.1.4")
    parser.addoption("--bv", default="105.0")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    executor_url = f"http://{executor}:4444/wd/hub"

    if executor == 'local':
        if browser_name == "chrome":
            driver = webdriver.Chrome(executable_path=DRIVER + "/chromedriver")
        elif browser_name == "opera":
            driver = webdriver.Opera(executable_path=DRIVER + "/operadriver")
        elif browser_name == "firefox":
            driver = webdriver.Firefox(executable_path=DRIVER + "/geckodriver")
        else:
            raise ValueError("Driver was not found!")

    else:
        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options":
                {
                    "enableVNC": True
                }
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    driver.maximize_window()

    request.addfinalizer(driver.close)
    return driver
