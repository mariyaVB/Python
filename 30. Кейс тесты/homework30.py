# Задача 1: напиши тестовые сценарии для данной функции и протестируйте ее
def calculate_average(numbers: list[float]) -> float:
    """
    Вычисляет среднее значение списка чисел.

    :param numbers: Список чисел
    :return: Среднее значение
    """
    if not numbers:
        raise ValueError("Список чисел не должен быть пустым")

    return sum(numbers) / len(numbers)


# test case 1
# expected result: calculate_average([2.6, 5, 7, 9, 11.4]) -> 7.0
# actual result: calculate_average([2.6, 5, 7, 9, 11.4]) -> 7.0
print(f'calculate_average([2.6, 5, 7, 9, 11.4]) -> {calculate_average([2.6, 5, 7, 9, 11.4])}')

# test case 2
# expected result: calculate_average([-2.0, 5, 7, -9, 11]) -> 2.4
# actual result: calculate_average([-2.0, 5, 7, -9, 11]) -> 2.4
print(f'calculate_average([-2.0, 5, 7, -9, 11]) -> {calculate_average([-2.0, 5, 7, -9, 11])}')


# test case 3
# expected result: calculate_average([2**2, 6]) -> 5
# actual result: calculate_average([-2.0, 5, 7, -9, 11]) -> 5
print(f'calculate_average([2 ** 2, 6]) -> {calculate_average([2 ** 2, 6])}')

# test case 4
# expected result: calculate_average() -> ValueError: Список чисел не должен быть пустым
# actual result: calculate_average() -> ValueError: Список чисел не должен быть пустым
# print(f'calculate_average([]) -> {calculate_average([])}')


# Задача 2: напиши тестовые сценарии для данной функции и протестируйте ее
def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0


# test case 1
# expected result: is_even(10) -> True
# actual result: is_even(10) -> True
print(f'is_even(10) -> {is_even(10)}')

# test case 2
# expected result: is_even(-10) -> True
# actual result: is_even(-10) -> True
print(f'is_even(-10) -> {is_even(-10)}')

# test case 3
# expected result: is_even(10.0) -> False
# actual result: is_even(10.0) -> True
print(f'is_even(10.0) -> {is_even(10.0)}')

# test case 4
# expected result: is_even(10.4) -> False
# actual result: is_even(10.4) -> False
print(f'is_even(10.4) -> {is_even(10.4)}')

# test case 5
# expected result: is_even(6 + 6) -> False
# actual result: is_even(6 + 6) -> False
number = 6 + 6
print(f'is_even({number}) -> {is_even(number)}')








