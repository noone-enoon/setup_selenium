from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import logging
import allure


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.fake = Faker()
        self._logger_config()

    def _logger_config(self):
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler("opencart.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=logging.INFO)

    @allure.step
    def open(self, path=''):
        self.logger.info("Open url: {}".format(path))
        self.driver.get(self.url + path)

    def _verify_element_presence(self, time, locator):
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.attach_screen_to_report()
            raise AssertionError("Can't find element for locator: {}".format(locator))

    def _verify_element_to_be_clickable(self, time, locator):
        try:
            return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.attach_screen_to_report()
            raise AssertionError("Can't click on element: {}".format(locator))

    def _verify_all_elements_presence(self, time, locator):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.attach_screen_to_report()
            raise AssertionError("Can't click on element: {}".format(locator))

    def _element(self, time, locator):
        return self._verify_element_presence(time, locator)

    def _elements(self, time, locator):
        return self._verify_all_elements_presence(time, locator)

    @allure.step
    def _click(self, time, locator):
        self.logger.info("Click on element: {}".format(locator))
        element = self._element(time, locator)
        element.click()

    @allure.step
    def _get_element_in_index(self, time, locator, index):
        self.logger.info("Get element: {} in index {}".format(locator, index))
        element = self._elements(time, locator)[index]
        return element

    @allure.step
    def _click_element(self, time, locator, index=0):
        self.logger.info("Click on element: {} in index {}".format(locator, index))
        element = self._get_element_in_index(time, locator, index)
        element.click()

    @allure.step
    def _send_keys(self, time, locator, text):
        self.logger.info("Send keys to element: {} with text {}".format(locator, text))
        element = self._element(time, locator)
        element.click()
        element.clear()
        element.send_keys(text)

    @allure.step
    def _close_alert(self):
        self.logger.info("Close alert")
        alert = self.driver.switch_to.alert
        alert.accept()

    def attach_screen_to_report(self, name="screen"):
        allure.attach(
            name=name,
            body=self.driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )
