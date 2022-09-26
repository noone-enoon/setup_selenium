from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
import allure


class Header(BasePage):
    SWITCH = (By.CSS_SELECTOR, "#top .pull-left .dropdown-toggle")
    DROPDOWN_MENU = (By.CSS_SELECTOR, "#top .pull-left .dropdown-menu li")

    @allure.step("Проверить, что курс валют именен")
    def check_exchange_rates(self, exchange_rate):
        icon_exchange_rate = exchange_rate.split(" ")[0]
        icon_exchange_rate_after_switch = self._element(2, self.SWITCH).text.split(" ")[0]
        return icon_exchange_rate == icon_exchange_rate_after_switch

    @allure.step("Сменить курс валют")
    def switch_exchange_rates(self):
        self._click(2, self.SWITCH)
        exchange_rate = self._get_element_in_index(2, self.DROPDOWN_MENU, 1).text
        self._click_element(2, self.DROPDOWN_MENU, 1)
        assert self.check_exchange_rates(exchange_rate) is True
