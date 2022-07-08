from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/admin"


class Page:
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".btn.btn-primary")
    HELP = (By.CSS_SELECTOR, ".help-block [href$='forgotten']")
    USER = (By.CSS_SELECTOR, ".fa.fa-user")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")


def test_catalog(driver, url):
    driver.get(url + path)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.BUTTON_LOGIN))
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.HELP))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.USER))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.INPUT_PASSWORD))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.INPUT_USERNAME))
