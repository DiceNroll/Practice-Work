num = int(input('Введите число: '))
for y in range(1, num + 1):
    for x in range(y):
        print(y, end='\t')
    print()
