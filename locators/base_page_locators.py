from selenium.webdriver.common.by import By


class BasePageLocators:
    # Кнопки хедера
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
