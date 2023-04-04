# МАРКИРОВКА ТЕСТОВ

# Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям,
# но также по каким-нибудь заданным нами категориям.
# Например, мы можем выбрать небольшое количество критичных тестов (smoke),
# которые нужно запускать на каждый коммит разработчиков, а остальные тесты обозначить как регрессионные (regression)
# и запускать их только перед релизом.
# Или у нас могут быть тесты, специфичные для конкретного браузера (internet explorer 11),
# и мы хотим запускать эти тесты только под данный браузер.
#
# Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks).
# Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка.

# Также в корневой директории тестового проекта нужно добавить файл pytest.ini
# и прописать в нём маркировки следующим образом:

# [pytest]
#  markers =
#      smoke: marker for smoke tests
#      regression: marker for regression tests  - текст после знака ":" является поясняющим — его можно не писать

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
# pytest -s -v -m smoke название_теста.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
