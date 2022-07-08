from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/laptop-notebook"


class Page:
    INPUT = (By.CSS_SELECTOR, "#input-sort")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
    PICTURE = (By.CSS_SELECTOR, ".product-thumb [title='MacBook Pro']")
    COMPARE = (By.CSS_SELECTOR, "#compare-total")
    HOME = (By.CSS_SELECTOR, "a[href$='common/home']")


def test_catalog(driver, url):
    driver.get(url + path)
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Page.INPUT))
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.LIST_VIEW))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.PICTURE))
    WebDriverWait(driver, 4).until(EC.element_to_be_clickable(Page.COMPARE))
    WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(Page.HOME))
