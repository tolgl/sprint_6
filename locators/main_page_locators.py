from selenium.webdriver.common.by import By


class MainPageLocators:
    title_questions = [By.XPATH, ".//div[@class='Home_FourPart__1uthg']/div"]
    question_1 = [By.ID, "accordion__heading-0"]
    answer_1 = [By.ID, "accordion__panel-0"]
    question_2 = [By.ID, "accordion__heading-1"]
    answer_2 = [By.ID, "accordion__panel-1"]
    question_3 = [By.ID, "accordion__heading-2"]
    answer_3 = [By.ID, "accordion__panel-2"]
    question_4 = [By.ID, "accordion__heading-3"]
    answer_4 = [By.ID, "accordion__panel-3"]
    question_5 = [By.ID, "accordion__heading-4"]
    answer_5 = [By.ID, "accordion__panel-4"]
    question_6 = [By.ID, "accordion__heading-5"]
    answer_6 = [By.ID, "accordion__panel-5"]
    question_7 = [By.ID, "accordion__heading-6"]
    answer_7 = [By.ID, "accordion__panel-6"]
    question_8 = [By.ID, "accordion__heading-7"]
    answer_8 = [By.ID, "accordion__panel-7"]
    panel_answer = [By.CLASS_NAME, "accordion__panel"]
    logo_yandex = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]