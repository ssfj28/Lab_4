# Задание 4. Рекурсивная проверка строки на палиндром.


def is_palindrome(text):
    """Проверяет, читается ли строка одинаково слева направо и справа налево."""
    if len(text) <= 1:  # Базовый случай.
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])  # Сравниваем внутреннюю часть строки.


source_text = input("Введите строку: ")
# Для проверки игнорируем регистр, пробелы и знаки препинания.
normalized_text = "".join(char.lower() for char in source_text if char.isalnum())

if is_palindrome(normalized_text):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
