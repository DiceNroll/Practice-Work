def dividers(num):
    d = [div for div in range(1, num + 1) if num % div == 0]
    return len(d) == 2


k = 0
for n in range(int(input('Введите кол-во чисел: '))):
    if dividers(int(input('Введите число: '))):
        k += 1

print('\nКоличество простых чисел в последовательности:', k)
