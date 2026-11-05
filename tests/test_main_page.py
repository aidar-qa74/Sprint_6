import allure
import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import MainPageData


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', MainPageData.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, driver, index, question, answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_block()
        question_received = main_page.click_on_question(index)
        answer_received = main_page.get_answer(index)
        # проверяем, что текст вопроса соответствует ожидаемому
        assert question_received == question, 'Вопрос на сайте не соответствует ожидаемому или в тексте есть ошибки'
        # проверяем, что текст ответа соответствует ожидаемому
        assert answer_received == answer, 'Ответ на сайте не соответствует ожидаемому или в тексте есть ошибки'

    @allure.title('Проверка кнопок "Заказать на Главной странице')
    @allure.description('Проверяем, что по клику на кнопку Заказать на Главной странице'
                        'открывается страница заказа')
    @pytest.mark.parametrize('loc', [MainPageLocators.HEADER_ORDER_BUTTON, MainPageLocators.FOOTER_ORDER_BUTTON])
    def test_order_button(self, driver, loc):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.scroll_to_element(loc)
        main_page.wait_for_load_element(loc)
        main_page.click_element(loc)
        main_page.wait_for_load_form()
        expected_url = main_page.get_url_order_page()
        assert driver.current_url == expected_url, 'URL не соответствует странице заказа'
