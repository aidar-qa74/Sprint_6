import allure
from pages.order_page import OrderPage
from pages.base_page import BasePage
from pages.main_page import MainPage


class TestRedirect:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката со страницы заказа')
    def test_open_main_page_when_click_on_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        base_page = BasePage(driver)
        base_page.click_on_logo_scooter()
        main_page= MainPage(driver)
        main_page.wait_for_load_page_title()
        expected_url = main_page.get_url_main_page()
        assert driver.current_url == expected_url, 'URL не соответствует главной странице'

    @allure.title('Проверка открытия нового окна страницы Дзена по клику на лого Яндекса')
    def test_open_dzen_in_new_window(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        base_page = BasePage(driver)
        base_page.click_on_logo_yandex()
        base_page.switch_to_new_window()
        base_page.wait_for_open_dzen()
        expected_url = base_page.get_url_dzen_page()
        assert driver.current_url == expected_url, 'URL не соответствует странице Дзена'
