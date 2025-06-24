def summ(n):
    return sum(map(int, str(n)))


maxi = 0
for x in range(int(input('Введите кол-во чисел: '))):
    num = input('Введите число: ')
    maxi = num if summ(num) > summ(maxi) else maxi
print('Число', maxi, 'имеет максимальную сумму цифр:', summ(maxi))
