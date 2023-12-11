from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

import allure


class MainPageHelper(BasePage):
    @allure.step("Скролл до блока FAQ")
    def scroll_to_block_questions(self):
        self.scroll_to_element(MainPageLocators.title_questions)

    @allure.step("Нажатие на вопрос")
    def click_on_question(self, question):
        self.find_element(question, wait_time=3).click()

    @allure.step("Получение ответа на вопрос")
    def get_answer_on_question(self, answer):
        return self.find_element(answer, wait_time=3).text

    @allure.step('Нажатие на кнопку Заказать в шапке сайта')
    def click_on_button_order_on_header(self):
        self.find_element(MainPageLocators.button_order_on_header, wait_time=3).click()

    @allure.step('Нажатие на кнопку Заказать внизу сайта')
    def click_on_button_order_on_footer(self):
        # скролл до кнопки "Заказать" внизу страницы
        self.scroll_to_element(MainPageLocators.button_order_on_footer)
        # клик по кнопке "Заказать"
        self.find_element(MainPageLocators.button_order_on_footer, wait_time=3).click()

    @allure.step('Получение заголовка на главной странице')
    def get_home_header(self):
        return self.find_element(MainPageLocators.home_header, wait_time=3).text
