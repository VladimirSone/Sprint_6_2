import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage

class OrderPage(BasePage):

    @allure.title('нажать на нопку Куки')
    def click_confirm_button(self):
        self.click_on_element(OrderPageLocators.confirm_button)

    @allure.title('клик по кнопке заказать')
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.button_order_2)

    @allure.title('ожидание загрузки страницы')
    def wait_for_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.order))

    @allure.title('ожидание загрузки кнопки Посмотреть статус ')
    def wait_check_status_order(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(OrderPageLocators.button_check_status_order))

    @allure.title('проверка появления кнопки Посмотреть статус')
    def check_button_status_order(self):
        self.driver.find_element(OrderPageLocators.button_check_status_order).is_displayed()

    @allure.title('заполнение полей на первой странице заказа')
    def order_data_form(self, USER_DATA):
        self.click_on_element(OrderPageLocators.name)  # нажать на поле имя
        self.driver.find_element(*OrderPageLocators.name).send_keys(USER_DATA[0])  # ввести имя
        self.click_on_element(OrderPageLocators.family)  # клик по полю фамилия
        self.driver.find_element(*OrderPageLocators.family).send_keys(USER_DATA[1])  # ввести фамилию
        self.click_on_element(OrderPageLocators.address)  # клик по полю адрес
        self.driver.find_element(*OrderPageLocators.address).send_keys(USER_DATA[2])  # ввести адрес
        self.click_on_element(OrderPageLocators.metro)  # клик по кнопке метро
        self.driver.find_element(*OrderPageLocators.metro).send_keys(USER_DATA[3])  # выбрать станцию метро
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)  # нажать на значение
        self.click_on_element(OrderPageLocators.phone)  # клик по полю телефон
        self.driver.find_element(*OrderPageLocators.phone).send_keys(USER_DATA[4])  # ввести номер телефона
        self.click_on_element(OrderPageLocators.button_next)  # клик по кнопке далее

    @allure.title('заполнение полей на второй странице заказа')
    def order_arend_form(self, USER_DATA):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(OrderPageLocators.title_page_rent_info))  # дождаться загрузки страницы
        self.click_on_element(OrderPageLocators.delivery_date)  # клик по полю когда привезут
        self.driver.find_element(*OrderPageLocators.delivery_date).send_keys(USER_DATA[5])  # ввести дату OK
        self.click_on_element(OrderPageLocators.checkbox_black_color_scooter)  # клик по чек=боксу черный OK
        self.click_on_element(OrderPageLocators.rental_period)  # клик по полю срок аренды ОК
        self.click_on_element(OrderPageLocators.dropdown_rental_period)  # клик по пункту выпадающего списка заказать OK
        self.click_on_element(OrderPageLocators.comment)  # клик по полю комментарий
        self.driver.find_element(*OrderPageLocators.comment).send_keys(USER_DATA[6])  # ввести комментарий
        self.click_on_element(OrderPageLocators.button_make_order)  # нажать на кнопку Заказать

    @allure.title('клик по кнопке Да')
    def button_yes_order(self):
        self.click_on_element(OrderPageLocators.button_yes_order)
