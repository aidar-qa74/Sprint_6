import allure

from data import Urls, OrderPageData

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем все поля для оформления заказа')
    def create_order(self, data_order):
        # Заполняем форму "Для кого самокат"
        self.set_value(OrderPageLocators.FIRST_NAME, data_order['first_name'])
        self.set_value(OrderPageLocators.LAST_NAME, data_order['last_name'])
        self.set_value(OrderPageLocators.ADDRESS, data_order['address'])
        self.set_metro_station(OrderPageLocators.STATION_METRO, data_order['station'])
        self.set_value(OrderPageLocators.TEL_NUMBER, data_order['tel_number'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        self.wait_for_load_element(OrderPageLocators.FORM2_TITLE)
        # Заполняем форму "Про аренду"
        self.set_value(OrderPageLocators.DATE_DELIVERY, data_order['delivery_date'])
        self.click_element(OrderPageLocators.SELECTED_DATE)
        self.wait_for_load_element(OrderPageLocators.RENT_TIME)
        self.set_rent_days(data_order['rent_days'])
        self.set_scooter_color(data_order['scooter_colour'])
        self.set_value(OrderPageLocators.COMMENT_FIELD, data_order['comment'])
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_load_element(OrderPageLocators.ORDER_CONFIRM)
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Вспомогательная функция для выбора станции')
    def set_metro_station(self, station):
        self.click_element(OrderPageLocators.STATION_METRO)
        method, station_loc = OrderPageLocators.SELECT_STATION
        station_locator_with_name = (method, station_loc.format(station))
        self.scroll_to_element(station_locator_with_name)
        self.click_element(station_locator_with_name)

    @allure.step('Вспомогательная функция для выбора срока аренды')
    def set_rent_days(self, rent_days):
        self.click_element(OrderPageLocators.RENT_TIME)
        method, rent_days_loc = OrderPageLocators.SELECT_RENT_TIME
        rent_days_locator_with_period = (method, rent_days_loc.format(rent_days))
        self.click_element(rent_days_locator_with_period)

    @allure.step('Вспомогательная функция для выбора цвета самоката')
    def set_scooter_color(self, scooter_color):
        method, checkbox_loc = OrderPageLocators.COLOR_CHECKBOX
        checkbox_locator_with_color = (method, checkbox_loc.format(scooter_color))
        self.click_element(checkbox_locator_with_color)

    @allure.step('Открываем страницу заказа')
    def open_order_page(self):
        self.open_page(Urls.ORDER_PAGE_URL)

    @allure.step('Ожидаем загрузки страницы заказа')
    def wait_for_load_form(self):
        self.wait_for_load_element(OrderPageLocators.FORM1_TITLE)

    @allure.step('Ожидаем появление окна "Заказ оформлен"')
    def wait_for_load_order_completed(self):
        self.wait_for_load_element(OrderPageLocators.ORDER_COMPLETED)

    @allure.step('Находим текст заголовка в окне подтверждения оформления заказа')
    def get_actual_result(self):
        actual_result = self.find_element(OrderPageLocators.ORDER_COMPLETED).text
        return actual_result

    @allure.step('Выводим ожидаемый результат текста заголовка')
    def get_expected_result(self):
        expected_result = OrderPageData.ORDER_CONFIRM_TITLE_TEXT
        return expected_result
    
    @allure.step('Получаем ожидаемый URL страницы заказа')
    def get_url_order_page(self):
        return Urls.ORDER_PAGE_URL
    

    

    

    

    
