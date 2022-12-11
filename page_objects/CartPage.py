from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    BUTTON_CART = (By.CSS_SELECTOR, "#button-cart")
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, "[data-original-title='Add to Wish List']")
    CALENDAR = (By.CSS_SELECTOR, ".input-group-btn .fa.fa-calendar")
    CONTROL_LABELS = (By.CSS_SELECTOR, ".control-label")
    IMAGE_HP = (By.CSS_SELECTOR, "[title='HP LP3065']")

    def check_clickable_button_cart(self):
        self._verify_element_to_be_clickable(2, self.BUTTON_CART)

    def check_clickable_add_to_wishlist(self):
        self._verify_element_to_be_clickable(2, self.ADD_TO_WISHLIST)

    def check_clickable_calendar(self):
        self._verify_element_to_be_clickable(2, self.CALENDAR)

    def check_visibility_image_hp(self):
        self._verify_element_presence(2, self.IMAGE_HP)

    def check_presence_of_all_elements_control_lists(self):
        self._verify_all_elements_presence(4, self.CONTROL_LABELS)
