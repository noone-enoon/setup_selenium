from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    HEART = (By.CSS_SELECTOR, "#top-links .fa.fa-heart")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search .input-group-btn")
    NAVBAR = (By.CSS_SELECTOR, ".nav.navbar-nav")
    TOTAL = (By.CSS_SELECTOR, "#cart-total")
    MAC_BOOK_AIR_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0 .swiper-slide-active [alt=MacBookAir]")


def test_wait_main(driver, url):
    driver.get(url)
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Page.TOTAL))
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located(Page.SEARCH_BUTTON))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.NAVBAR))
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located(Page.HEART))
    WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(Page.MAC_BOOK_AIR_SLIDESHOW))
