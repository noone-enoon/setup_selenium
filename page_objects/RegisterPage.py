from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class RegisterPage(BasePage):
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "[type=submit][value=Continue]")
    HREF_LOGIN = (By.CSS_SELECTOR, "[href$='login']")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    SUBSCRIBE_YES = (By.CSS_SELECTOR, ".radio-inline [name=newsletter][value='1']")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    CHECKBOX = (By.CSS_SELECTOR, "[type=checkbox]")
    HREF_SUCCESS_REGISTER = (By.CSS_SELECTOR, "[href$='route=account/account']")

    def check_clickable_compare_button_continue(self):
        self._verify_element_to_be_clickable(2, self.BUTTON_CONTINUE)

    def check_clickable_compare_subscribe_yes(self):
        self._verify_element_to_be_clickable(2, self.SUBSCRIBE_YES)

    def check_visibility_input_firstname(self):
        self._verify_element_presence(2, self.INPUT_FIRSTNAME)

    def check_visibility_input_telephone(self):
        self._verify_element_presence(2, self.INPUT_TELEPHONE)

    def check_presence_of_all_elements_href_login(self):
        self._verify_all_elements_presence(2, self.HREF_LOGIN)

    @allure.step("Зарегистрировать пользователя")
    def register_account(self, email=None, password=None):
        if not email:
            email = self.fake.email()
        if not password:
            password = self.fake.text(9)

        self._send_keys(7, self.INPUT_FIRSTNAME, self.fake.name().split(" ")[0])
        self._send_keys(2, self.INPUT_LASTNAME, self.fake.name().split(" ")[1])
        self._send_keys(2, self.INPUT_EMAIL, email)
        self._send_keys(2, self.INPUT_TELEPHONE, self.fake.phone_number())
        self._send_keys(2, self.INPUT_PASSWORD, password)
        self._send_keys(2, self.INPUT_CONFIRM, password)
        self._click(2, self.CHECKBOX)
        self._click(2, self.BUTTON_CONTINUE)
        self._verify_element_presence(3, self.HREF_SUCCESS_REGISTER)
