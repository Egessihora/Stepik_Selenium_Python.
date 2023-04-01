# MODUL 3. LESSON 2. TASK 13

# Тестирование с помощью unittest:

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
# Если работаем в PyCharm, не забываем выбрать в настройках unnitest в качестве test-runner!!


# Создаём класс, который должен наследоваться от класса TestCase
class TestRegistration(unittest.TestCase):
    # Превращаем тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции
    def test_registration_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Код, который заполняет обязательные поля
            input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
            input1.send_keys("Anastasiya")
            input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
            input2.send_keys("Begunova")
            input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
            input3.send_keys("ABmail@mail.ru")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # Записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # С помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error login")

        finally:
            # Закрываем браузер после всех манипуляций
            browser.quit()

        if __name__ == "__main__":
            unittest.main()

    def test_registration_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
            input1.send_keys("Anastasiya")
            input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
            input2.send_keys("Begunova")
            input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
            input3.send_keys("ABmail@mail.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error login")

        finally:
            browser.quit()

        if __name__ == "__main__":
            unittest.main()
