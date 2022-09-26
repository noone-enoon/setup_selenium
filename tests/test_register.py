from page_objects.RegisterPage import RegisterPage
import allure

path = "/index.php?route=account/register"


@allure.title("Ожидания элементов на странице регистрации")
def test_wait_register(driver, url):
    register_page = RegisterPage(driver, url)
    register_page.open(path)
    register_page.check_clickable_compare_button_continue()
    register_page.check_clickable_compare_subscribe_yes()
    register_page.check_visibility_input_firstname()
    register_page.check_visibility_input_telephone()
    register_page.check_presence_of_all_elements_href_login()


@allure.title("Регистрация пользователя")
def test_register_account(driver, url):
    register_page = RegisterPage(driver, url)
    register_page.open(path)
    register_page.register_account()
