import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import UserData
from locator.order_page_locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.title('нажать на нопку Куки')
    def click_confirm_button(self):
        self.driver.find_element(*OrderPageLocators.confirm_button).click()

    @allure.title('проскроллить до кнопки заказать')
    def scroll_to_section_questions(self):
        element = self.driver.find_element(*OrderPageLocators.button_order_2)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.title('клик по кнопке заказать')
    def click_button_order(self):
        self.driver.find_element(*OrderPageLocators.button_order_2).click()

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
    def order_data_form(self, user_data):
        self.driver.find_element(*OrderPageLocators.name).click()  # нажать на поле имя
        self.driver.find_element(*OrderPageLocators.name).send_keys(user_data[0])  # ввести имя
        self.driver.find_element(*OrderPageLocators.family).click()  # клик по полю фамилия
        self.driver.find_element(*OrderPageLocators.family).send_keys(user_data[1])  # ввести фамилию
        self.driver.find_element(*OrderPageLocators.address).click()  # клик по полю адрес
        self.driver.find_element(*OrderPageLocators.address).send_keys(user_data[2])  # ввести адрес
        self.driver.find_element(*OrderPageLocators.metro).click()  # клик по кнопке метро
        self.driver.find_element(*OrderPageLocators.metro).send_keys(user_data[3])  # выбрать станцию метро
        self.driver.find_element(*OrderPageLocators.select_item_in_dropdown_metro).click()  # нажать на значение
        self.driver.find_element(*OrderPageLocators.phone).click()  # клик по полю телефон
        self.driver.find_element(*OrderPageLocators.phone).send_keys(user_data[4])  # ввести номер телефона
        self.driver.find_element(*OrderPageLocators.button_next).click()  # клик по кнопке далее

    @allure.title('заполнение полей на второй странице заказа')
    def order_arend_form(self, user_data):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(OrderPageLocators.title_page_rent_info))  # дождаться загрузки страницы
        self.driver.find_element(*OrderPageLocators.delivery_date).click()  # клик по полю когда привезут
        self.driver.find_element(*OrderPageLocators.delivery_date).send_keys(user_data[5])  # ввести дату OK
        self.driver.find_element(*OrderPageLocators.checkbox_black_color_scooter).click()  # клик по чек=боксу черный OK
        self.driver.find_element(*OrderPageLocators.rental_period).click()  # клик по полю срок аренды ОК
        self.driver.find_element(*OrderPageLocators.dropdown_rental_period).click()  # клик по пункту выпадающего списка заказать OK
        self.driver.find_element(*OrderPageLocators.comment).click()  # клик по полю комментарий
        self.driver.find_element(*OrderPageLocators.comment).send_keys(user_data[6])  # ввести комментарий
        self.driver.find_element(*OrderPageLocators.button_make_order).click()  # нажать на кнопку Заказать

    @allure.title('клик по кнопке Да')
    def button_yes_order(self):
        self.driver.find_element(*OrderPageLocators.button_yes_order).click()
