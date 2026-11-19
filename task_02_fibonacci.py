# Задание 2. Рекурсивное вычисление n-го числа Фибоначчи.

from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """Возвращает n-е число Фибоначчи (F(0) = 0, F(1) = 1)."""
    if n == 0:  # Первый базовый случай.
        return 0
    if n == 1:  # Второй базовый случай.
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивный случай.


number = int(input("Введите неотрицательный номер числа Фибоначчи n: "))

if number < 0:
    print("Ошибка: номер должен быть неотрицательным.")
else:
    print(f"Число Фибоначчи F({number}) = {fibonacci(number)}")
