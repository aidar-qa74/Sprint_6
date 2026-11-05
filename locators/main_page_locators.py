from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_TITLE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
    # Локаторы на основной странице
    FAQ_LIST = [By.CLASS_NAME, "accordion"]
    FAQ_QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    FAQ_ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]

    # Локаторы кнопок Заказать
    HEADER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[1]"]
    FOOTER_ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]
