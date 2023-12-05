from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_block_questions(self):
        element = self.driver.find_element(*MainPageLocators.title_questions)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_panel_questions(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "accordion")))

    def click_on_question_and_get_answer(self, question, answer):
        self.wait_panel_questions()
        self.driver.find_element(*question).click()
        return self.driver.find_element(*answer).text

    def click_logo_yandex_and_get_current_url(self):
        self.driver.find_element(*MainPageLocators.logo_yandex).click()
        # ожидаем появление второй вкладки
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))
        # переключаемся на вторую вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # ожидаем появление логотипа "Дзен"
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "desktop-base-header__logoBrand-3W")))
        # получаем текущий url
        return self.driver.current_url
