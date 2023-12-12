# https://leetcode.com/problems/happy-number/description/


def some_func():
    """
    Функция принимает числовое значение от пользователя, считает
    сумму квадратов цифр этого числа и потом число изменяется на
    сумму его квадратов, цикл нужно проделать до тех пор, пока
    сумма квадратов числа n не станет равна 1, тогда возвращаем True,
    в случае же бесконечного цикла нужно вернуть False.
    """
    n = int(input())

    k = set()

    while n != 1 and n not in k:
        k.add(n)
        digits = [int(digit) for digit in str(n)]

        squared_digits = [digit**2 for digit in digits]

        sum_squarres = sum(squared_digits)

        n = sum_squarres

    return n == 1


a = some_func()

print(a)
