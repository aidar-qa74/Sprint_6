import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)

    @allure.step('Прокручиваем вниз страницу до блока "Вопросы о важном", ожидаем загрузку блока')
    def scroll_to_block(self):
        self.scroll_to_element(MainPageLocators.FAQ_LIST)
        self.wait_for_load_element(MainPageLocators.FAQ_LIST)

    @allure.step('Ожидаем, пока прогрузится форма заказа')
    def wait_for_load_form(self):
        self.wait_for_load_element(OrderPageLocators.FORM1_TITLE)

    @allure.step('Вспомогательная функция для получения текста вопроса в блоке "Вопросы о важном"')
    def click_on_question(self, index):
        method, locator = MainPageLocators.FAQ_QUESTION
        locator = locator.format(index)
        self.wait_for_load_element((method, locator))
        question = self.find_element((method, locator))
        question.click()
        return question.text

    @allure.step('Вспомогательная функция для получения текста ответа в блоке "Вопросы о важном"')
    def get_answer(self, index):
        method, locator = MainPageLocators.FAQ_ANSWER
        locator = locator.format(index)
        self.wait_for_load_element((method, locator))
        return self.find_element((method, locator)).text

    @allure.step('Получаем ожидаемый URL страницы заказа')
    def get_url_order_page(self):
        return Urls.ORDER_PAGE_URL
