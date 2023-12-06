import time

from selenium import webdriver
from pages.order_page import OrderPage
import allure


class TestMakeOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.fullscreen_window()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.title('Проверка оформления заказа по кнопке "Заказать" вверху страницы')
    def test_make_order_on_header(self):
        # объект класса страницы оформления заказа
        order_page = OrderPage(self.driver)
        # метод нажатия на кнопку "Заказать" в хедере
        order_page.click_on_button_order_on_header()
        # метод заполнения формы оформления заказа
        order_page.filling_order_form('Тест', 'Тестов', 'ул. Тестовая, 15', '89999999999')
        # метод получения текста на форме успешного оформления заказа
        actual_result = order_page.get_text_successful_order()

        assert 'Заказ оформлен' in actual_result

    @allure.title('Проверка оформления заказа по кнопке "Заказать" внизу страницы')
    def test_make_order_on_footer(self):
        # объект класса страницы оформления заказа
        order_page = OrderPage(self.driver)
        # метод нажатия на кнопку "Заказать" внизу страницы
        order_page.click_on_button_order_on_footer()
        # метод заполнения формы оформления заказа
        order_page.filling_order_form('Тест', 'Тестов', 'ул. Тестовая, 15', '89999999999')
        # метод получения текста на форме успешного оформления заказа
        actual_result = order_page.get_text_successful_order()

        assert 'Заказ оформлен' in actual_result

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
