from page_objects.CatalogPage import CatalogPage

path = "/laptop-notebook"


def test_wait_catalog(driver, url):
    catalog_page = CatalogPage(driver, url)
    catalog_page.open(path)
    catalog_page.check_clickable_compare_element()
    catalog_page.check_clickable_list_view_element()
    catalog_page.check_visibility_input()
    catalog_page.check_visibility_picture()
    catalog_page.check_presence_of_all_elements_home()
