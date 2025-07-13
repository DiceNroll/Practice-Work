from math import log, exp, floor, ceil

for n in range(int(input('Введите кол-во чисел: '))):
    num = float(input('Введите число: '))
    if num < 0: print('x =', floor(num), 'exp(x) =', exp(floor(num)))
    if num > 0: print('x =', ceil(num), 'log(x) =', log(ceil(num)))
