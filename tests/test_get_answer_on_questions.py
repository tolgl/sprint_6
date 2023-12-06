import pytest
from selenium import webdriver
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
import allure


class TestGetAnswer:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.fullscreen_window()

    @allure.title('Проверка текста ответов на блоке "Вопросы о важном"')
    @pytest.mark.parametrize(
        'locator_question,locator_answer,expected_result',
        [
            [MainPageLocators.question_1, MainPageLocators.answer_1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
            [MainPageLocators.question_2, MainPageLocators.answer_2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
            [MainPageLocators.question_3, MainPageLocators.answer_3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
            [MainPageLocators.question_4, MainPageLocators.answer_4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
            [MainPageLocators.question_5, MainPageLocators.answer_5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
            [MainPageLocators.question_6, MainPageLocators.answer_6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
            [MainPageLocators.question_7, MainPageLocators.answer_7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
            [MainPageLocators.question_8, MainPageLocators.answer_8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
        ]
    )
    def test_get_answer(self, locator_question, locator_answer, expected_result):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        # объект класса главной страницы
        main_page = MainPage(self.driver)
        # скролл до блока с вопросами
        main_page.scroll_to_block_questions()
        # нажатие на вопрос и получение ответа на вопрос
        actual_result = main_page.click_on_question_and_get_answer(locator_question, locator_answer)

        assert actual_result == expected_result

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
