from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    HEART = (By.CSS_SELECTOR, "#top-links .fa.fa-heart")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search .input-group-btn")
    NAVBAR = (By.CSS_SELECTOR, ".nav.navbar-nav")
    TOTAL = (By.CSS_SELECTOR, "#cart-total")
    MAC_BOOK_AIR_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0 .swiper-slide-active [alt=MacBookAir]")

    def check_visibility_heart(self):
        self._verify_element_presence(2, self.HEART)

    def check_visibility_search_button(self):
        self._verify_element_presence(2, self.SEARCH_BUTTON)

    def check_visibility_navbar(self):
        self._verify_element_presence(2, self.NAVBAR)

    def check_visibility_total(self):
        self._verify_element_presence(2, self.TOTAL)

    def check_presence_of_all_elements_slidehow(self):
        self._verify_all_elements_presence(5, self.MAC_BOOK_AIR_SLIDESHOW)
