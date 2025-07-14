def test(n):
    if n > 0: positive()
    if n < 0: negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


test(int(input('Введите число: ')))
