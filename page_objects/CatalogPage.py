from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    INPUT = (By.CSS_SELECTOR, "#input-sort")
    LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
    PICTURE = (By.CSS_SELECTOR, ".product-thumb [title='MacBook Pro']")
    COMPARE = (By.CSS_SELECTOR, "#compare-total")
    HOME = (By.CSS_SELECTOR, "a[href$='common/home']")

    def check_clickable_list_view_element(self):
        self._verify_element_to_be_clickable(2, self.LIST_VIEW)

    def check_clickable_compare_element(self):
        self._verify_element_to_be_clickable(2, self.COMPARE)

    def check_visibility_input(self):
        self._verify_element_presence(1, self.INPUT)

    def check_visibility_picture(self):
        self._verify_element_presence(2, self.PICTURE)

    def check_presence_of_all_elements_home(self):
        self._verify_all_elements_presence(5, self.HOME)
