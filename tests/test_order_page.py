import allure
import pytest
from conftest import driver
from data import UserData
from locator.main_page_locators import MainPageLocators
from page_objects.order_page import OrderPage

class TestOrderPageOrder:
    @allure.title('Проверка позитивного оформления заказа')
    @pytest.mark.parametrize('button, USER_DATA', [(MainPageLocators.button_order_in_header, UserData.USER_DATA_0), (MainPageLocators.button_order_in_main, UserData.USER_DATA_1)])
    def test_order_page_order(self, driver, button, USER_DATA):
        order_page = OrderPage(driver)
        order_page.click_confirm_button()  # нажать на кнопку куки
        order_page.scroll_to_element(button)  # проскроллить до кнопки "Заказать"
        order_page.click_button_order()  # нажать на кнопку Заказать
        order_page.wait_for_order()  # дождаться загрузки страницы Заказать
        order_page.order_data_form(USER_DATA)  # ввести данные для заказа на первой странице
        order_page.order_arend_form(USER_DATA)  # ввести данные для заказа на второй странице
        order_page.button_yes_order()  # нажать кнопку Да в появившемся окне
        assert order_page.check_button_status_order
