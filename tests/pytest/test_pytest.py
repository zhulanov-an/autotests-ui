def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) != 5


class TestUser:
    def test_1(self):
        print("test_1")

    def test_2(self):
        print("test_2")

    def test_3(self):
        print("test_3")
