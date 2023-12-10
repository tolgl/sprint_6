import datetime

import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPageHelper(BasePage):

    @allure.step("Заполнение формы заказа")
    def filling_order_form(self, name, surname, address, phone):
        # заполняем поле "Имя"
        self.find_element(OrderPageLocators.name, wait_time=3).send_keys(name)
        # заполняем поле "Фамилия"
        self.find_element(OrderPageLocators.surname, wait_time=3).send_keys(surname)
        # заполняем поле "Адрес"
        self.find_element(OrderPageLocators.address, wait_time=3).send_keys(address)
        # клик на поле "Станция метро"
        self.find_element(OrderPageLocators.metro_station, wait_time=3).click()
        # клик на выпадающий список поля "Станция метро"
        self.find_element(OrderPageLocators.metro_station_value, wait_time=3).click()
        # заполняем поле "Телефон"
        self.find_element(OrderPageLocators.phone, wait_time=3).send_keys(phone)
        # клик на кнопку "Далее" на форме "Для кого самокат"
        self.find_element(OrderPageLocators.button_next, wait_time=3).click()
        # заполняем поле "Когда привезти самокат" текущей датой
        self.find_element(OrderPageLocators.date_delivery, wait_time=3).send_keys(datetime.date.today().strftime('%d.%m.%Y'))
        # имитация клика на клавишу Enter
        self.find_element(OrderPageLocators.date_delivery, wait_time=3).send_keys(u'\ue007')
        # клик на поле "Срок аренды"
        self.find_element(OrderPageLocators.rental_period, wait_time=3).click()
        # клик на значение выпадающего списка "Срок аренды"
        self.find_element(OrderPageLocators.rental_period_list, wait_time=3).click()
        # клик на чекбокс выбора цвета самоката
        self.find_element(OrderPageLocators.color, wait_time=3).click()
        # клик на кнопку "Заказать" на форме "Про аренду"
        self.find_element(OrderPageLocators.button_order_on_form, wait_time=3).click()
        # клик на кнопку "Да" на форме подтверждения заказа
        self.find_element(OrderPageLocators.button_confirmation_order, wait_time=3).click()

    @allure.step("Получение текста успешного оформления заказа")
    def get_text_successful_order(self):
        return self.find_element(OrderPageLocators.successful_order_header, wait_time=3).text



