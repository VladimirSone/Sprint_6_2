import allure
import pytest
from conftest import driver
from data import UserData
from locator.main_page_locators import MainPageLocators
from page_objects.order_page import OrderPage

class TestOrderPageOrder:
    @allure.title('Проверка позитивного оформления заказа')
    @pytest.mark.parametrize('button, user_data', [(MainPageLocators.button_order_in_header, UserData.user_data_0), (MainPageLocators.button_order_in_main, UserData.user_data_1)])
    def test_order_page_order(self, driver, button, user_data):
        order_page = OrderPage(driver)
        order_page.click_confirm_button()  # нажать на кнопку куки
        order_page.scroll_to_section_questions()  # проскроллить до кнопки заказать
        order_page.click_button_order()  # нажать на кнопку Заказать
        order_page.wait_for_order()  # дождаться загрузки страницы Заказать
        order_page.order_data_form(user_data)  # ввести данные для заказа на первой странице
        order_page.order_arend_form(user_data)  # ввести данные для заказа на второй странице
        order_page.button_yes_order()  # нажать кнопку Да в появившемся окне
        assert order_page.check_button_status_order
