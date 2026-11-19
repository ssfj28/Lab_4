# Задание 5. Рекурсивный бинарный поиск в отсортированном списке.


def binary_search(numbers, target, left, right):
    """Возвращает индекс target или -1, если элемент не найден."""
    if left > right:  # Базовый случай: диапазон поиска пуст.
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle
    if target < numbers[middle]:
        return binary_search(numbers, target, left, middle - 1)
    return binary_search(numbers, target, middle + 1, right)


numbers = [int(value) for value in input(
    "Введите целые числа через пробел (в возрастающем порядке): "
).split()]

if numbers != sorted(numbers):
    print("Ошибка: список должен быть отсортирован по возрастанию.")
else:
    target = int(input("Введите искомое число: "))
    result = binary_search(numbers, target, 0, len(numbers) - 1)

    if result == -1:
        print("Элемент не найден.")
    else:
        print(f"Элемент найден. Индекс (нумерация с нуля): {result}")
