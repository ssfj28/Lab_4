# Задание 8. Рекурсивный подсчёт количества цифр в целом числе.


def count_digits(number):
    """Возвращает количество цифр в числе, не учитывая знак минус."""
    number = abs(number)
    if number < 10:  # Базовый случай: осталось одна цифра, включая число 0.
        return 1
    return 1 + count_digits(number // 10)  # Убираем последнюю цифру.


number = int(input("Введите целое число: "))
print(f"Количество цифр в числе {number}: {count_digits(number)}")
