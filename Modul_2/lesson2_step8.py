# MODUL 2. LESSON 2. TASK 8

# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input.form-control[name='firstname']").send_keys("Anastasiya")
    browser.find_element(By.CSS_SELECTOR, "input.form-control[name='lastname']").send_keys("Begunova")
    browser.find_element(By.CSS_SELECTOR, "input.form-control[name='email']").send_keys("ABmail@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # загружаемый файл должен находится в одной директории с исполняемым файлом
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.ID, "file").send_keys(file_path)  # находим кнопку для добавления файла и добавляем файл

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
