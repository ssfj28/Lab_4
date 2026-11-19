# Задание 9. Рекурсивное решение головоломки «Ханойская башня».


def hanoi(disks, source, destination, auxiliary):
    """Выводит последовательность ходов и возвращает их количество."""
    if disks == 0:  # Базовый случай: перемещать нечего.
        return 0

    moves = hanoi(disks - 1, source, auxiliary, destination)
    print(f"Переместить диск {disks}: {source} -> {destination}")
    moves += 1
    moves += hanoi(disks - 1, auxiliary, destination, source)
    return moves


number_of_disks = int(input("Введите количество дисков (целое число больше 0): "))

if number_of_disks <= 0:
    print("Ошибка: количество дисков должно быть положительным.")
else:
    print("Последовательность перемещений:")
    total_moves = hanoi(number_of_disks, "A", "C", "B")
    print(f"Всего перемещений: {total_moves}")
    print(f"Минимальное число ходов по формуле 2^n - 1: {2 ** number_of_disks - 1}")
