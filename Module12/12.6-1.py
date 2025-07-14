def summa(n):
    print('Сумма чисел от 1 до', n, 'равна', sum([i for i in range(1, n + 1)]))


summa(int(input('Введите число: ')))
