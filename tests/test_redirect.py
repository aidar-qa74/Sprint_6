import allure
from pages.order_page import OrderPage


class TestRedirect:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката со старницы заказа')
    def test_open_main_page_when_click_on_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_scooter()
        order_page.wait_for_load_page_title()
        expected_url = order_page.get_url_main_page()
        assert driver.current_url == expected_url, 'URL не соответствует главной странице'

    @allure.title('Проверка открытия нового окна станицы Дзена по клику на лого Яндекса')
    def test_open_dzen_in_new_window(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_yandex()
        order_page.switch_to_new_window()
        order_page.wait_for_open_dzen()
        expected_url = order_page.get_url_dzen_page()
        assert driver.current_url == expected_url, 'URL не соответствует странице Дзена'
