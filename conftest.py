from selenium import webdriver
import pytest

DRIVER = "C:\drivers_automation"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.1.7:8081/")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path=DRIVER + "/chromedriver")
    elif browser_name == "opera":
        browser = webdriver.Opera(executable_path=DRIVER + "/operadriver")
    elif browser_name == "firefox":
        browser = webdriver.Firefox(executable_path=DRIVER + "/geckodriver")
    else:
        raise ValueError("Driver was not found!")
    request.addfinalizer(browser.close)
    return browser
