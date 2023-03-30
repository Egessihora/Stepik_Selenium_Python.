# MODUL 4. LESSON 4. TASK 7

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
        # element_to_be_clickable вернёт элемент, когда он станет кликабельным, или вернет False в ином случае
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(2)
    browser.quit()
    
# Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться, когда кнопка станет кликабельной.
# Для реализации подобных ожиданий в Selenium WebDriver существует понятие явных ожиданий (Explicit Waits),
# которые позволяют задать специальное ожидание для конкретного элемента.
# Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и expected_conditions.
