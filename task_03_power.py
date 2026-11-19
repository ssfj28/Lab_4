# Задание 3. Рекурсивное возведение числа x в целую степень n.


def power(x, n):
    """Вычисляет x в степени n рекурсивным способом."""
    if n == 0:  # Базовый случай: любое ненулевое число в нулевой степени равно 1.
        return 1
    if n < 0:
        if x == 0:
            raise ZeroDivisionError("Ноль нельзя возвести в отрицательную степень.")
        return 1 / power(x, -n)
    return x * power(x, n - 1)  # Рекурсивный случай.


base = float(input("Введите основание x: "))
exponent = int(input("Введите целую степень n: "))

try:
    print(f"Результат: {base} ** {exponent} = {power(base, exponent)}")
except ZeroDivisionError as error:
    print(f"Ошибка: {error}")
