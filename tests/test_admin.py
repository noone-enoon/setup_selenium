from page_objects.AdminPage import AdminPage

path = "/admin"


def test_wait_admin(driver, url):
    admin_page = AdminPage(driver, url)
    admin_page.open(path)
    admin_page.check_clickable_help_element()
    admin_page.check_clickable_user_element()
    admin_page.check_visibility_button_login()
    admin_page.check_visibility_input_password()
    admin_page.check_visibility_input_username()


def test_add_to_cart(driver, url):
    admin_page = AdminPage(driver, url)
    admin_page.open(path)
    admin_page.login_admin()
    item_name = admin_page.add_item()
    assert admin_page.check_add_item(item_name) is True


def test_delete_item(driver, url):
    admin_page = AdminPage(driver, url)
    admin_page.open(path)
    admin_page.login_admin()
    item_name = admin_page.add_item()
    admin_page.delete_item(item_name)
