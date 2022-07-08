from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/laptop-notebook/hp-lp3065"


class Page:
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    CALENDAR = (By.CSS_SELECTOR, ".input-group-btn .fa.fa-calendar")
    CONTROL_LABELS = (By.CSS_SELECTOR, ".control-label")
    IMAGE_HP = (By.CSS_SELECTOR, "[title='HP LP3065']")


def test_catalog(driver, url):
    driver.get(url + path)
    WebDriverWait(driver, 1).until(EC.element_to_be_clickable(Page.BUTTON_CART))
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.ADD_TO_WISHLIST))
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Page.CALENDAR))
    WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located(Page.CONTROL_LABELS))
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Page.IMAGE_HP))
