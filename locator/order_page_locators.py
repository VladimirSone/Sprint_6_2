from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Экран "Для кого самокат"
    title_page_personal_info = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    name = (By.XPATH, "//input[@placeholder='* Имя']")
    family = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    select_item_in_dropdown_metro = (By.XPATH, ".//li[@class='select-search__row']")
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")

    # Экран "Про аренду"
    title_page_rent_info = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    delivery_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    checkbox_black_color_scooter = (By.XPATH, "//input[@id='black']")
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Подтверждение заказа
    button_yes_order = (By.XPATH, "//button[text()='Да']")
    button_check_status_order = (By.XPATH, './/button[text()="Посмотреть статус"]')

    # кнопка Заказать внизу
    button_order_2 = (By.XPATH, '/html/body/div/div/div/div[4]/div[2]/div[5]/button')  # (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # заголовок страницы Заказать "Для кого самокат"
    order = (By.XPATH, './/div[text()="Для кого самокат"]')

    # кнопка куки
    confirm_button = (By.XPATH, './/*[@id="rcc-confirm-button"]')