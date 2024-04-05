import math
import unittest


def line():
    print('-------------------------------------------------------------------------------------------------------')


def calculate_square_circle(radius_circle):
    pi = 3.14159
    square = radius_circle * pi
    return square


def valid_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return calculate_square_triangle(a, b, c)
    else:
        print('Треугольник не существует.')
        return False


def calculate_square_triangle(a, b, c):
    sides = [a, b, c]
    hypotenuse = max(sides)
    sides.remove(hypotenuse)

    if hypotenuse**2 != sides[0]**2 + sides[1]**2:

        p = (a + b + c) / 2
        square = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'Площадь равностороннего треугольника равна: {square} (см в квадрате)')
        return square

    if hypotenuse**2 == sides[0]**2 + sides[1]**2:
        square = 0.5 * sides[0] * sides[1]
        print(f'Площадь прямоугольного треугольника равна: {square} (см в квадрате)')
        return square


while True:
    command = input('Вычислить площадь круга 1\n'
                    'Вычислить площадь треугольника 2\n'
                    'Выход 0\n'
                    'Ответ: _____')
    line()

    match command:
        case '1':
            radius = float(input('радиус окружности: _____ (см в квадрате)'))
            print(f'Площадь окружности с радиусом {radius} равна {calculate_square_circle(radius)} (см в квадрате).')
            line()
        case '2':
            side_a = float(input('сторона треугольника a: _____ (см в квадрате)'))
            side_b = float(input('сторона треугольника b: _____ (см в квадрате)'))
            side_c = float(input('сторона треугольника c: _____ (см в квадрате)'))
            valid_triangle(side_a, side_b, side_c)
            line()

        case '0':
            break


class TestGetSquare(unittest.TestCase):
    def test_square_circle(self):
        self.assertEqual(calculate_square_circle(10), 31.4159)

    def test_square_right_triangle(self):
        self.assertEqual(calculate_square_triangle(3, 4, 5), 6)

    def test_square_triangle(self):
        self.assertEqual(calculate_square_triangle(3, 7, 5), 6.49519052838329),

    def test_valid_triangle(self):
        self.assertFalse(valid_triangle(1, 1, 3))


if __name__ == '__main__':
    unittest.main()