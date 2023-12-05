from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage
import allure


class TestClickLogo:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.fullscreen_window()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.title('Проверка нажатия на логотип "Самокат" на странице заказа')
    def test_click_logo_scooter_on_page_order(self):
        # объект класса страницы оформления заказа
        order_page = OrderPage(self.driver)
        # метод нажатия на кнопку "Заказать"
        order_page.click_on_button_order_on_header()
        # метод нажатия на логотип "Самокат"
        order_page.click_logo_scooter()
        # метод получения заголовка главной страницы
        actual_result = order_page.get_home_header()

        assert f'Самокат\nна пару дней' in actual_result

    @allure.title('Проверка нажатия на логотип "Яндекс" на странице заказа')
    def test_click_logo_yandex_on_main_page(self):
        # объект класса страницы оформления заказа
        main_page = MainPage(self.driver)
        # функция нажатия на логотип "Яндекс" и получения текущего url
        actual_result = main_page.click_logo_yandex_and_get_current_url()

        assert 'dzen.ru' in actual_result

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
