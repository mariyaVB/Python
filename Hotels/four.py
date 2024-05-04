# Задача 4. Написать метод, который в консоль выводит таблицу умножения.
# На вход метод получает число, до которого выводит таблицу умножения.
# В консоли должна появиться таблица.

def return_multiplication_table(number):
    if number > 0:
        for multiplier1 in range(1, number+1):
            for multiplier2 in range(1, number+1):
                print("%-5d" % (multiplier1 * multiplier2), end='')
            print()
    else:
        print('error')


return_multiplication_table(5)
