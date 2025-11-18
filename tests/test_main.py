from hello import greet


def test_greet():
    assert greet("World") == "Hello, World!"


def test_greet_fails_intentional():
    # намеренно падающий тест — можно убрать перед финальной записью
    assert greet("Alice") == "Hello, Alice!"
