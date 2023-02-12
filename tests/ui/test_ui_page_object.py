from modules.ui.page_objects.sign_in_page import SignInRage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкта сторінки
    sign_in_page = SignInRage()

    # відкриваємо сторінку http://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриємо браузер
    sign_in_page.close()
