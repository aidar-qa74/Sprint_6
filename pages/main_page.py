import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)

    @allure.step('Прокручиваем вниз страницу до блока "Вопросы о важном", ожидаем загрузку блока')
    def scroll_to_block(self):
        self.scroll_to_element(MainPageLocators.FAQ_LIST)
        self.wait_for_load_element(MainPageLocators.FAQ_LIST)

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

    @allure.step('Ожидаем загрузки заголовка "Самокат на пару дней" на главной странице')
    def wait_for_load_page_title(self):
        self.wait_for_load_element(MainPageLocators.PAGE_TITLE)

    @allure.step('Получаем ожидаемый URL главной страницы')
    def get_url_main_page(self):
        return Urls.MAIN_PAGE_URL
