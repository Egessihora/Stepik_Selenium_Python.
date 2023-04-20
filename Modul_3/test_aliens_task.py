# MODUL 3. LESSON 6. TASK 5.
#
# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
# Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
# Ваша задача — реализовать автотест со следующим сценарием действий:
#
# открыть страницу
# авторизоваться на странице со своим логином и паролем
# ввести правильный ответ (поле перед вводом должно быть пустым)
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

# Правильным ответом на задачу в заданных шагах является число:
# # import time
# import math
# # answer = math.log(int(time.time()))

# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
# # https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
#
# Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания,
# чтобы тесты работали стабильно.
#
# В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке
# не совпадает со строкой "Correct!"
# Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
#
# Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено
# правильное локальное время (https://time.is/ru/).
# Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.

# РЕШЕНИЕ:

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import time
import math


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
class TestAliens:
    def test_aliens_task(self, browser, links):
        # Логинимся
        link = links
        browser.get(link)
        browser.implicitly_wait(30)  # ждём прогрузки страницы (неявное ожидание)

        button_enter = browser.find_element(By.ID, "ember33")  # нажимаем на кнопку авторизации на сайте
        button_enter.click()

        input_email = browser.find_element(By.ID, "id_login_email")  # вводим логин
        input_email.send_keys("egessa@yandex.ru")

        input_password = browser.find_element(By.ID, "id_login_password")
        input_password.send_keys("gecatonboyon1000stepik")  # вводим пароль

        button_login = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")  # нажимаем на кнопку "Войти"
        button_login.click()
        time.sleep(10)

        # -----------------------------------------------------------------------------------------------------------
        # Вводим ответ
        try:
            # Если кнопка "Решить снова" есть
            browser.implicitly_wait(10)
            button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
            button_again.click()

            # Если кнопки "Решить снова" нет
        except NoSuchElementException:
            print('Кнопка "Решить снова" отсутствует')

        finally:
            # Находим поле ввода ответа
            time.sleep(20)
            input_answer = browser.find_element(By.TAG_NAME, 'textarea')
            input_answer.clear()

            # Вычисляем ответ
            # Если ваше время не совпадает со временем на сайте, то смотрим на сайте отображаемую разницу
            answer = math.log(int(time.time()) - 0.034)
            answer_text = str(answer)

            # Вводим и отправляем ответ
            input_answer.send_keys(answer_text)
            time.sleep(5)
            button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
            button_send.click()

            # Проверяем ответ
            browser.implicitly_wait(10)
            answer_feedback = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
            assert answer_feedback.text == "Correct!", "Wrong answer!"
