from selenium.webdriver.common.by import By

class MainPageLocators:
    # логотип на главной странице
    scooter_logo = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')  # логотип самокат
    yandex_logo = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')  # логотип Яндекс

    # заголовок на главной странице Самокат
    page_heading = (By.XPATH, '//div[@class="Home_Header__iJKdX"]')

    # заголовок страницы Заказать "Для кого самокат"
    order = (By.XPATH, './/div[text()="Для кого самокат"]')

    # логотип страницы Дзен
    logo_dzen = By.XPATH, './/symbol/path[1]'

    # раздел вопросы о важном - сделать параметризацию
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')
    # список вопросов
    list_question ={
        1: [By.XPATH, './/div [@id ="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, './/div [@id ="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, './/div [@id ="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, './/div [@id ="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, './/div [@id ="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, './/div [@id ="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, './/div [@id ="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, './/div [@id ="accordion__heading-7"]/parent::div']
    }

    # текст под стрелочками - сделать параметризацию
    answers_question_all = {
        1: (By.XPATH, '//div [@id ="accordion__panel-0"]'),
        2: (By.XPATH, '//div [@id ="accordion__panel-1"]'),
        3: (By.XPATH, '//div [@id ="accordion__panel-2"]'),
        4: (By.XPATH, '//div [@id ="accordion__panel-3"]'),
        5: (By.XPATH, '//div [@id ="accordion__panel-4"]'),
        6: (By.XPATH, '//div [@id ="accordion__panel-5"]'),
        7: (By.XPATH, '//div [@id ="accordion__panel-6"]'),
        8: (By.XPATH, '//div [@id ="accordion__panel-7"]')
    }

    # Кнопки Заказать на главной странице
    button_order_in_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    button_order_in_header = (By.XPATH, '//button[text() = "Заказать"]')