from selenium.webdriver.common.by import By


class OrderPageLocators:
    # 1-я форма страницы заказа
    FORM1_TITLE = [By.XPATH, "//div[contains(@class, 'Order_Header')]"]
    FIRST_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    STATION_METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    SELECT_STATION = [By.XPATH, ".//div[text()='{}']"]
    TEL_NUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    # 2-я форма страницы заказа 
    FORM2_TITLE = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    SELECTED_DATE = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    RENT_TIME = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]
    SELECT_RENT_TIME = [By.XPATH, ".//div[text()='{}']"]
    COLOR_CHECKBOX = [By.ID, '{}']
    COMMENT_FIELD = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]
    # Всплывающее окно подтверждения оформления заказа
    ORDER_CONFIRM = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    # Окно "Заказ оформлен"
    ORDER_COMPLETED = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]

