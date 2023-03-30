# MODUL 2. LESSON 4. TASK 3, 5

# Тестовый сценарий выглядит так:
#
# Открыть страницу http://suninjuly.github.io/wait1.html
# Нажать на кнопку "Verify"
# Проверить, что появилась надпись "Verification was successful!"

# Для открытия страницы мы используем метод get, затем находим нужную кнопку с помощью одного из методов
# find_element_by_ и нажимаем на нее с помощью метода click.
# Далее находим новый элемент с текстом и проверяем соответствие текста на странице ожидаемому тексту.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(2)
    browser.quit()

# С методом implicitly_wait() при небольших задержках в работе сайта тесты продолжат работать стабильно.
# На каждый вызов команды find_element WebDriver будет ждать заданное количество секунд
# до появления элемента на странице прежде, чем выбросить исключение NoSuchElementException.
