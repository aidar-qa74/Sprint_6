from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Открываем страницу
    def open_page(self, page_url):
        self.driver.get(page_url)

    # Ожидание загрузки элемента
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    # Ожидание открытия страницы при переходе по ссылке
    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(page_url))

    # Ищем элемент
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # Кликаем на элемент
    def click_element(self, locator):
        self.find_element(locator).click()

    # Вводим текст в поле
    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    # Скролл страницы до элемента
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # Переключаемся на новую вкладку
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
