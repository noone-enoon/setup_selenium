from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/index.php?route=account/register"


class Page:
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "[type=submit][value=Continue]")
    HREF_LOGIN = (By.CSS_SELECTOR, "[href$='login']")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    SUBSCRIBE_YES = (By.CSS_SELECTOR, ".radio-inline [name=newsletter][value='1']")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")


def test_catalog(driver, url):
    driver.get(url + path)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.BUTTON_CONTINUE))
    WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(Page.HREF_LOGIN))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.INPUT_FIRSTNAME))
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.SUBSCRIBE_YES))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.INPUT_TELEPHONE))
