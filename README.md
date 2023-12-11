# Автотесты для сервиса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)
*В проекте использовался фреймворк Selenium, Pytest и Allure*


1. Файл locators/main_page_locators.py содержит локаторы блока FAQ
1. Файл locators/order_page_locators.py содержит локаторы формы оформления заказа
1. Файл pages/main_page.py содержит методы:
   - __scroll_to_block_questions__ - скролл до блока FAQ
   - __wait_panel_questions__ - ожидает появление панели с вопросами
   - __click_on_question_and_get_answer__ - кликает по всем вопросам на блоке FAQ и возвращает ответ
   - __click_logo_yandex_and_get_current_url__ - кликает на лого Яндекс и возвращает текущий url
1. Файл pages/order_page.py содержит методы:
   - __click_on_button_order_on_header__ - нажимает на кнопку "Заказать" в шапке сайта
   - __click_on_button_order_on_footer__ - нажимает на кнопку "Заказать" внизу страницы
   - __filling_order_form__ - заполняет форму оформления заказа
   - __get_text_successful_order__ - возвращает текст успешно оформленного заказа
   - __click_logo_scooter__ - кликает на логотип Самокат
   - __get_home_header__ - возвращает заголовок на главной странице
1. Файл test_open_constructor_from_personal_account содержит автотесты перехода на главную страницу из ЛК:
   - __test_successful_redirection_to_constructor_from_personal_account__ - проверяет переход на главную из ЛК кликом по ссылке "Конструктор"
   - __test_successful_redirection_to_main_page_click_on_logo__ - проверяет переход на главную из ЛК кликом по логотипу
1. Файл tests/test_get_answer_on_questions.py содержит автотест:
   - __test_get_answer__ - проверяет текст ответа на вопрос на блоке FAQ, используя параметризацию
1. Файл tests/test_click_logo.py содержит автотесты:
   - __test_click_logo_scooter_on_page_order__ - проверяет переход на главную страницу
   - __test_click_logo_yandex_on_main_page__ - проверяет переход на страницу дзена
1. Файл tests/test_make_order.py содержит автотесты:
   - __test_make_order_on_header__ - проверяет оформление заказа из кнопки "Заказать" в шапке сайта
   - __test_make_order_on_footer__ - проверяет оформление заказа из кнопки "Заказать" внизу страницы
1. Папка Allure_results/result_test_click_logo содержит результат тестирования нажатия на лого Яндекс и Самокат
1. Папка Allure_results/result_test_make_order содержит результат тестирования оформления заказа
1. Папка Allure_results/result_test_get_answer_on_questions содержит результат тестирования получения ответов на блоке FAQ