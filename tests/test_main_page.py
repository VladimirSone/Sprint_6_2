import allure
import pytest
from conftest import driver
from page_objects.main_page import MainPage
from data import UserData

class TestMainPageQuestion:
    @allure.title('Проверка разделов "Вопросы о важном')
    @allure.title('Проверка появления текста при нажатии на нужный вопрос')
    @pytest.mark.parametrize('question_number,expected_answer', UserData.data_expected_answer)
    def test_main_page_question(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_section_questions()  # скролл до раздела "Вопросы о важном"
        main_page.wait_visibility_faq_section()  # дождаться загрузки раздела вопросов
        main_page.click_question_1(question_number)  # нажать на вопросы
        main_page.wait_visibility_answers_question_all(question_number)  # дождаться загрузки ответов на вопрос
        assert main_page.check_text_answers_question_all
