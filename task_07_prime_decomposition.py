# Задание 7. Рекурсивное разложение числа на сумму простых чисел.

from functools import lru_cache
from math import isqrt


def get_primes(number):
    """Формирует список простых чисел от 2 до number включительно."""
    primes = []
    for candidate in range(2, number + 1):
        is_prime = True
        for divisor in range(2, isqrt(candidate) + 1):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
    return primes


def decompose_into_primes(number):
    """Находит одно разложение number на простые слагаемые.

    Слагаемые возвращаются в порядке убывания. Одно и то же простое
    число может использоваться несколько раз.
    """
    primes = get_primes(number)

    @lru_cache(maxsize=None)
    def find_sum(remaining, max_index):
        if remaining == 0:  # Базовый случай: сумма составлена полностью.
            return ()
        if remaining < 2 or max_index < 0:
            return None

        for index in range(min(max_index, len(primes) - 1), -1, -1):
            prime = primes[index]
            if prime <= remaining:
                # max_index не уменьшается: простое слагаемое можно повторять.
                result = find_sum(remaining - prime, index)
                if result is not None:
                    return (prime,) + result
        return None

    return find_sum(number, len(primes) - 1)


number = int(input("Введите целое число N (N >= 2): "))

if number < 2:
    print("Ошибка: число должно быть не меньше 2.")
else:
    decomposition = decompose_into_primes(number)
    print(f"Разложение числа {number} на простые слагаемые:")
    print(" + ".join(map(str, decomposition)), "=", number)
