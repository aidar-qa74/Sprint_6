from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
from locators.base_page_locators import BasePageLocators 
from data import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')
    def open_page(self, page_url):
        self.driver.get(page_url)

    @allure.step('Ожидание загрузки элемента')
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание открытия страницы при переходе по ссылке')
    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(page_url))

    @allure.step('Ищем элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на элемент')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Вводим текст в поле')
    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step('Скролл страницы до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Кликаем на лого Самоката')
    def click_on_logo_scooter(self):
        self.click_element(BasePageLocators.SCOOTER_BUTTON)

    @allure.step('Кликаем на лого Яндекса')
    def click_on_logo_yandex(self):
        self.click_element(BasePageLocators.YANDEX_BUTTON)

    @allure.step('Ожидаем открытия страницы Дзена')
    def wait_for_open_dzen(self):
        self.wait_for_open_page(Urls.DZEN_URL)

    @allure.step('Получаем ожидаемый URL страницы Дзена')
    def get_url_dzen_page(self):
        return Urls.DZEN_URL