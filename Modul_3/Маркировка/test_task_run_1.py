# Отметьте ниже только те тестовые методы, которые будут найдены и выполнены PyTest при запуске следующей команды:
# pytest -v -m "smoke and not beta_users" test_task_run_1.py

import pytest


class TestMainPage():
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login(self, browser):
        assert True

    # номер 2
    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket(self, browser):
        assert True


class TestBasket():
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page(self, browser):
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_guest_can_see_total_price(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket(self, browser):
        assert True

    # номер 6
    @pytest.mark.regression
    def test_guest_can_see_book_price(self, browser):
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue(browser):
    assert True

# Ответ: 1 и 4

# 1-й отмечен маркировками:
# smoke - то, что указано в команде запуска.
# xfail - отмечает, что тест провальный. она не повлияет на результат тестирования, но и не отменяет запуск теста.
# Тест запустится.

# 2-й отмечен маркировкой regression, отсутствуещей в команде запуска.
# Тест не запустится.

# 3-й отмечен маркировками:
# skip с параметром reason="not implemented yet" - отмечает пропуск теста, с причиной (reason) "еще не реализовано"
# smoke - есть в команде запуска, но из-за маркировки skip будет пропущен
# Тест не запустится.

# 4-й отмечени маркировкой smoke, имеющейся в команде запуска.
# Тест запустится.

# 5-й и 6-й отмечены маркировками smoke и regression, но из-за наличия маркировки skip на всё классе этих тестов
# будут пропущены
# Тесты не запустятся.

# 7-й отмечен маркировками:
# beta_users, на которую стоит запрет (not) в команде запуска,
# smoke - есть в команде запуска, но из-за маркировки beta_users не запустится.
# Тесты не запустятся.
