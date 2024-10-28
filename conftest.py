import pytest
from selenium import webdriver

#  фикстура веб-драйвера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.window('--window-size=1920,1080')
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
