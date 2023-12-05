import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_button_order_on_header(self):
        self.driver.find_element(*OrderPageLocators.button_order_on_header).click()

    def click_on_button_order_on_footer(self):
        element = self.driver.find_element(*OrderPageLocators.button_order_on_footer)
        # скролл до кнопки "Заказать" внизу страницы
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # ожидание появления кнопки "Заказать"
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.button_order_on_footer))
        self.driver.find_element(*OrderPageLocators.button_order_on_footer).click()

    def filling_order_form(self, name, surname, address, phone):
        # заполняем поле "Имя"
        self.driver.find_element(*OrderPageLocators.name).send_keys(name)
        # заполняем поле "Фамилия"
        self.driver.find_element(*OrderPageLocators.surname).send_keys(surname)
        # заполняем поле "Адрес"
        self.driver.find_element(*OrderPageLocators.address).send_keys(address)
        # клик на поле "Станция метро"
        self.driver.find_element(*OrderPageLocators.metro_station).click()
        # клик на выпадающий список поля "Станция метро"
        self.driver.find_element(*OrderPageLocators.metro_station_value).click()
        # заполняем поле "Телефон"
        self.driver.find_element(*OrderPageLocators.phone).send_keys(phone)
        # клик на кнопку "Далее" на форме "Для кого самокат"
        self.driver.find_element(*OrderPageLocators.button_next).click()
        # заполняем поле "Когда привезти самокат" текущей датой
        self.driver.find_element(*OrderPageLocators.date_delivery).send_keys(datetime.date.today().strftime('%d.%m.%Y'))
        # имитация клика на клавишу Enter
        self.driver.find_element(*OrderPageLocators.date_delivery).send_keys(u'\ue007')
        # клик на поле "Срок аренды"
        self.driver.find_element(*OrderPageLocators.rental_period).click()
        # клик на значение выпадающего списка "Срок аренды"
        self.driver.find_element(*OrderPageLocators.rental_period_list).click()
        # клик на чекбокс выбора цвета самоката
        self.driver.find_element(*OrderPageLocators.color).click()
        # клик на кнопку "Заказать" на форме "Про аренду"
        self.driver.find_element(*OrderPageLocators.button_order_on_form).click()
        # клик на кнопку "Да" на форме подтверждения заказа
        self.driver.find_element(*OrderPageLocators.button_confirmation_order).click()

    def get_text_successful_order(self):
        return self.driver.find_element(*OrderPageLocators.successful_order_header).text

    def click_logo_scooter(self):
        self.driver.find_element(*OrderPageLocators.logo_scooter).click()

    def get_home_header(self):
        return self.driver.find_element(*OrderPageLocators.home_header).text








