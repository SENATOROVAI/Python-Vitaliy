# https://leetcode.com/problems/happy-number/description/
"""Данный модуль предназначен для проверки не является ли число счастливым."""


def is_happy_num() -> bool:
    """Функция принимает числовое значение от пользователя, считает сумму
    квадратов цифр этого числа и потом число изменяется на сумму его квадратов,
    цикл нужно проделать до тех пор, пока сумма квадратов числа n не станет
    равна 1, тогда возвращаем True, в случае же бесконечного цикла нужно
    вернуть False."""
    num = int(input())

    set_k = set()

    while num != 1 and num not in set_k:
        set_k.add(num)
        digits = [int(digit) for digit in str(num)]

        squared_digits = [digit**2 for digit in digits]

        sum_squarres = sum(squared_digits)

        num = sum_squarres

    return num == 1


ANSWER: bool = is_happy_num()

print(ANSWER)
