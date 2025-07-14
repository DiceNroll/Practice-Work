def test(n, act):
    if act == 1: summa(n)
    if act == 2: maxi(n)
    if act == 3: mini(n)


def summa(n):
    print('\nСумма цифр:', sum(map(int, str(n))))


def maxi(n):
    print('\nМаксимальная цифра:', max([i for i in str(n)]))


def mini(n):
    print('\nМаксимальная цифра:', min([i for i in str(n)]))


while True:
    num = int(input('Введите число: '))
    act = int(input('\nВведите номер действия:\n1 - Сумма цифр\n2 - Максимальная цифр\n3 - Минимальная цифра: '))
    test(num, act)

# Безусловно, можно было бы и засунуть оба инпута в вызов функции, но это просто нечитаемая дичь будет ¯\_(ツ)_/¯