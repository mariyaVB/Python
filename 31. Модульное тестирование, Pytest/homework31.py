import pytest


# Задача 1: напиши тестовые сценарии для данной функции и протестируйте ее с помощью pytest
def calculate_average(numbers: list[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)


def test_base_calculate_average():
    expected_result = 7.0
    actual_result = calculate_average([2.6, 5, 7, 9, 11.4])
    assert expected_result == actual_result


def test_with_negative_values():
    expected_result = 2.4
    actual_result = calculate_average([-2.0, 5, 7, -9, 11])
    assert expected_result == actual_result


def test_list_with_mathematical_actions():
    expected_result = 5
    actual_result = calculate_average([2**2, 6])
    assert expected_result == actual_result


def test_with_error():
    with pytest.raises(ValueError):
        calculate_average([])


# Задача 2: напиши тестовые сценарии для данной функции и протестируйте ее с помощью pytest
def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0


def test_base_is_even():
    expected_result = True
    actual_result = is_even(10)
    assert expected_result == actual_result


def test_negative_numbers_is_even():
    expected_result = True
    actual_result = is_even(-10)
    assert expected_result == actual_result


def test_float_is_even():
    expected_result = False
    actual_result = is_even(10.4)
    assert expected_result == actual_result







