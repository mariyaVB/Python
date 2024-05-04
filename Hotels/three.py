# Задача 3. Написать функцию/метод, которая возвращает массив простых чисел в диапазоне
# (2 числа - минимальное и максимальное) заданных чисел.
# Например, на вход переданы 2 числа: от 11 до 20 (диапазон считается включая граничные значения).
# На выходе программа должна выдать [11, 13, 17, 19]
import sympy


def returns_prime_numbers(start, end):
    if start >= 0 and (end > 0 and end > start):
        answer = []
        for element in range(start, end+1):
            if sympy.isprime(element):
                answer.append(element)

        return answer

    else:
        return 0


print(returns_prime_numbers(-11, 20))
