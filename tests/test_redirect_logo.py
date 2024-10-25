import allure
from conftest import driver
from page_objects.main_page import MainPage

class TestLogo:

    @allure.title('Проверка перехода наглавную страницу сервиса по клику на логотип Самокат')
    def test_redirect_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_button_order()  # ожидание загрузки кнопки Заказать
        main_page.click_button_order()  # нажать на кнопку Заказать
        main_page.wait_for_order()  # ожидание страницы Заказать
        main_page.click_scooter_logo()  # нажать на логотип самокат
        main_page.wait_for_page_heading()  # заголовок на главной странице Самокат
        assert main_page.check_displaying_of_page_heading

    @allure.title('Проверка переъода на страницу Дзен по клику на логотип Яндекс')
    def test_redirect_logo_yandex(self,driver):
        main_page = MainPage(driver)
        main_page.wait_for_yandex_logo()  # ожидание загрузки логотипа Яндекс
        main_page.click_yandex_logo()  # нажать на логотип Яндекс
        main_page.switch_to_next_tab()  # активировать новую вкладку
        assert main_page.check_displaying_of_logo_dzen  # проверка, что загрузилась страница Дзен(проверяется логотип Дзен)