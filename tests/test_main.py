from page_objects.MainPage import MainPage
from page_objects.elements.Header import Header


def test_wait_main(driver, url):
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.check_visibility_heart()
    main_page.check_visibility_navbar()
    main_page.check_visibility_total()
    main_page.check_visibility_search_button()
    main_page.check_presence_of_all_elements_slidehow()


def test_switch_exchange_rates(driver, url):
    header = Header(driver, url)
    header.open()
    header.switch_exchange_rates()
