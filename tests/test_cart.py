from page_objects.CartPage import CartPage
import allure

path = "/laptop-notebook/hp-lp3065"


@allure.title("Ожидания элементов на странице карточки продукта")
def test_wait_cart(driver, url):
    cart_page = CartPage(driver, url)
    cart_page.open(path)
    cart_page.check_clickable_add_to_wishlist()
    cart_page.check_clickable_button_cart()
    cart_page.check_clickable_calendar()
    cart_page.check_visibility_image_hp()
    cart_page.check_presence_of_all_elements_control_lists()
