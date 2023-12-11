import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Открытие страницы Яндекс Самокат')
    def go_to_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator, wait_time=3)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_open_new_window(self, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(expected_conditions.number_of_windows_to_be(2))

    @allure.step('Переключение на новое окно')
    def switch_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Нажатие на логотип Самокат')
    def click_logo_scooter(self):
        return self.find_element(BasePageLocators.logo_scooter, wait_time=3).click()

    @allure.step('Нажатие на логотип Яндекс')
    def click_logo_yandex(self):
        return self.find_element(BasePageLocators.logo_yandex, wait_time=3).click()

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

