# Задача 2. Написать функцию/метод, которая на вход получает массив положительных целых чисел произвольной длины.
# Например [42, 12, 18]. На выходе возвращает массив чисел, которые являются общими делителями для всех указанных числе.
# В примере это будет [2, 3, 6].
import math

a = [14, 28, 42]
b = [42, 12, 18]
c = [20, 40, 60, 80]


def find_common_divisor(list_number):
    divisors = []
    answer = []
    for el_number in list_number:
        i = 2
        while i <= el_number:
            if el_number % i == 0:
                divisors.append(i)
            i += 1

    for el_divisor in divisors:
        if divisors.count(el_divisor) == len(list_number):
            answer.append(el_divisor)

    return list(set(answer))


print(find_common_divisor(a))
print(find_common_divisor(b))
print(find_common_divisor(c))
