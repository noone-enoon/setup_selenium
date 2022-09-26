from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class AdminPage(BasePage):
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".btn.btn-primary")
    HELP = (By.CSS_SELECTOR, ".help-block [href$='forgotten']")
    USER = (By.CSS_SELECTOR, ".fa.fa-user")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_USERNAME = (By.CSS_SELECTOR, "#input-username")
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    MENU_PRODUCTS = (By.LINK_TEXT, "Products")
    BUTTON_ADD_NEW = (By.CSS_SELECTOR, "#content .pull-right a[data-original-title='Add New']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_META_TAG = (By.CSS_SELECTOR, "#input-meta-title1")
    MENU_ADD_PRODUCT = (By.CSS_SELECTOR, ".nav.nav-tabs li")
    INPUT_MODEL = (By.CSS_SELECTOR, "#input-model")
    PRODUCT_LIST = (By.CSS_SELECTOR, "#form-product")
    FILTER_INPUT_NAME = (By.CSS_SELECTOR, "#input-name")
    BUTTON_FILTER = (By.CSS_SELECTOR, "#button-filter")
    CHECKBOX_PRODUCT = (By.CSS_SELECTOR, ".table-responsive input[type='checkbox']")
    BUTTON_DELETE = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
    TEXT_NO_RESULTS = (By.XPATH, "//form[contains(@id, 'form-product')]//tr/td[contains(text(), 'No results!')]")

    def check_visibility_button_login(self):
        self._verify_element_presence(2, self.BUTTON_LOGIN)

    def check_visibility_input_password(self):
        self._verify_element_presence(2, self.INPUT_PASSWORD)

    def check_visibility_input_username(self):
        self._verify_element_presence(2, self.INPUT_USERNAME)

    def check_clickable_help_element(self):
        self._verify_element_to_be_clickable(2, self.HELP)

    def check_clickable_user_element(self):
        self._verify_element_to_be_clickable(2, self.USER)

    @allure.step("Авторизоваться под пользователем")
    def login_admin(self):
        self._send_keys(2, self.INPUT_USERNAME, 'user')
        self._send_keys(2, self.INPUT_PASSWORD, 'bitnami')
        self._click(1, self.BUTTON_SUBMIT)

    @allure.step("Добавить новый продукт в админ-панель")
    def add_item(self):
        item_name = self.fake.text(9)
        self._click(1, self.MENU_CATALOG)
        self._click(1, self.MENU_PRODUCTS)
        self._click(1, self.BUTTON_ADD_NEW)
        self._send_keys(1, self.INPUT_NAME, item_name)
        self._send_keys(1, self.INPUT_META_TAG, self.fake.text(6))
        self._click_element(1, self.MENU_ADD_PRODUCT, 1)
        self._send_keys(1, self.INPUT_MODEL, self.fake.text(6))
        self._click(1, self.BUTTON_SUBMIT)
        return item_name

    @allure.step("Проверить, что продукт добавлен")
    def check_add_item(self, item_name):
        all_items = self._element(1, self.PRODUCT_LIST).text
        if item_name in all_items:
            return True

    @allure.step("Отфильтровать по имени")
    def filtering_products_by_name(self, name):
        self._send_keys(1, self.FILTER_INPUT_NAME, name)
        self._click(1, self.BUTTON_FILTER)

    def check_product_deleted(self):
        self._verify_element_presence(2, self.TEXT_NO_RESULTS)

    @allure.step("Удалить элемент")
    def delete_item(self, name):
        self._click(1, self.MENU_CATALOG)
        self._click(1, self.MENU_PRODUCTS)
        self.filtering_products_by_name(name)
        self._click_element(1, self.CHECKBOX_PRODUCT, 1)
        self._click(1, self.BUTTON_DELETE)
        self._close_alert()
        self.check_product_deleted()
