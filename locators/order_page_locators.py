from selenium.webdriver.common.by import By


class OrderPageLocators:
    button_order_on_header = [By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']"]
    button_order_on_footer = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"]
    name = [By.XPATH, ".//input[@placeholder='* Имя']"]
    surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]
    metro_station_value = [By.CLASS_NAME, "select-search__select"]
    phone = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]
    button_next = [By.XPATH, ".//div[@class = 'Order_NextButton__1_rCA']/button"]
    date_delivery = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    rental_period = [By.CLASS_NAME, "Dropdown-control"]
    rental_period_list = [By.XPATH, ".//div[@class='Dropdown-menu']/div[text()='двое суток']"]
    color = [By.ID, "black"]
    button_order_on_form = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"]
    button_confirmation_order = [By.XPATH, ".//button[text()='Да']"]
    successful_order_header = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    logo_scooter = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    home_header = [By.CLASS_NAME, "Home_Header__iJKdX"]