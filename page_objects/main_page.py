import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    @allure.title('ожидание загрузки кнопки Заказать(вверху страницы)')
    def wait_for_button_order(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.button_order_in_header))

    @allure.title('нажать кнопку Заказать')
    def click_button_order(self):
        self.click_on_element(MainPageLocators.button_order_in_header)

    @allure.title('ожидание страницы Заказать')
    def wait_for_order(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.order))

    @allure.title('нажать логотип самокат')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.scooter_logo)

    @allure.title('ожижание главной страницы Самокат')
    def wait_for_page_heading(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.page_heading))

    @allure.title('проверка, что загрузилась главная страница Самокат (заголовок страницы)')
    def check_displaying_of_page_heading(self):
        return self.driver.find_element(MainPageLocators.page_heading).is_displayed()

    #  тест проверка логотип Яндекс
    @allure.title('ожидание загрузки логотипа Яндекс')
    def wait_for_yandex_logo(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(
            MainPageLocators.yandex_logo))

    @allure.title('нажать на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.yandex_logo)

    @allure.title('открытие новой вкладки')
    def switch_to_next_tab(self):
        self.driver.switch_to.new_window(self.driver.window_handles[1])

    @allure.title('проверка, что загрузилась страница Дзен')
    def check_displaying_of_logo_dzen(self):
        return self.driver.find_element(MainPageLocators.logo_dzen).is_displayed()

    # тест проверка раздела "Вопросы о важном"

    @allure.title('проскроллить до раздела вопросы')
    def scroll_to_section_questions(self):
        element = self.driver.find_element(*MainPageLocators.faq_section)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.title('клик по вопросам')
    def click_question_1(self,data):
        self.click_on_element(MainPageLocators.list_question[data])

    @allure.title('ожидание загрузки раздела вопросы')
    def wait_visibility_faq_section(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(MainPageLocators.faq_section))

    @allure.title('ожидание загрузки текстов при клике на вопросы')
    def wait_visibility_answers_question_all(self, data):  # дождаться загрузки ответов
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(MainPageLocators.answers_question_all[data]))

    @allure.title('проверить, что при клике на нужный вопрос появляется текст')
    def check_text_answers_question_all(self, data):
        return self.driver.find_element(MainPageLocators.answers_question_all[data]).is_displayed()
