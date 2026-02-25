def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")


def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) != 5  # Тут должна быть ошибка


class TestUser:
    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")
