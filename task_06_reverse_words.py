# Задание 6. Рекурсивное изменение порядка слов на обратный.


def reverse_words(words):
    """Возвращает список слов в обратном порядке с помощью рекурсии."""
    if len(words) <= 1:  # Базовый случай.
        return words
    return reverse_words(words[1:]) + [words[0]]


text = input("Введите несколько слов: ")
words = text.split()
reversed_text = " ".join(reverse_words(words))

print("Строка с обратным порядком слов:", reversed_text)
