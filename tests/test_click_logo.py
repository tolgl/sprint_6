from locators.base_page_locators import BasePageLocators
from pages.main_page import MainPageHelper
from pages.base_page import BasePage
import allure


class TestClickLogo:
    @allure.title('Проверка нажатия на логотип "Самокат" на странице заказа')
    def test_click_logo_scooter_on_page_order(self, driver):
        # объект класса страницы оформления заказа
        main_page = MainPageHelper(driver)
        # открытие страницы
        main_page.go_to_page()
        # метод нажатия на кнопку "Заказать"
        main_page.click_on_button_order_on_header()
        # метод нажатия на логотип "Самокат"
        base_page = BasePage(driver)
        base_page.click_logo_scooter()
        # метод получения заголовка главной страницы
        actual_result = main_page.get_home_header()

        assert f'Самокат\nна пару дней' in actual_result

    @allure.title('Проверка нажатия на логотип "Яндекс" на главной странице')
    def test_click_logo_yandex_on_main_page(self, driver):
        # объект класса страницы оформления заказа
        main_page = MainPageHelper(driver)
        # открытие страницы
        main_page.go_to_page()

        base_page = BasePage(driver)
        # нажатие на логотип Яндекс
        base_page.click_logo_yandex()
        # ожидания открытия нового окна
        base_page.wait_open_new_window(wait_time=3)
        # переключение на новое окно
        base_page.switch_new_window()
        # ищем логотип Дзен
        base_page.find_element(BasePageLocators.logo_dzen)
        # получение текущего url
        actual_result = base_page.get_current_url()

        assert 'dzen.ru' in actual_result
