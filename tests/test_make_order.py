from pages.main_page import MainPageHelper
from pages.order_page import OrderPageHelper
import allure


class TestMakeOrder:

    @allure.title('Проверка оформления заказа по кнопке "Заказать" вверху страницы')
    def test_make_order_on_header(self, driver):
        # объект класса главной страницы
        main_page = MainPageHelper(driver)
        # открытие страницы
        main_page.go_to_page()
        # метод нажатия на кнопку "Заказать" в хедере
        main_page.click_on_button_order_on_header()
        # метод заполнения формы оформления заказа
        order_page = OrderPageHelper(driver)
        order_page.filling_order_form('Тест', 'Тестов', 'ул. Тестовая, 15', '89999999999')
        # метод получения текста на форме успешного оформления заказа
        actual_result = order_page.get_text_successful_order()

        assert 'Заказ оформлен' in actual_result

    @allure.title('Проверка оформления заказа по кнопке "Заказать" внизу страницы')
    def test_make_order_on_footer(self, driver):
        # объект класса главной страницы
        main_page = MainPageHelper(driver)
        # открытие страницы
        main_page.go_to_page()
        # метод нажатия на кнопку "Заказать" внизу страницы
        main_page.click_on_button_order_on_footer()
        # метод заполнения формы оформления заказа
        order_page = OrderPageHelper(driver)
        order_page.filling_order_form('Тест', 'Тестов', 'ул. Тестовая, 15', '89999999999')
        # метод получения текста на форме успешного оформления заказа
        actual_result = order_page.get_text_successful_order()

        assert 'Заказ оформлен' in actual_result
