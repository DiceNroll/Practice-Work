height = int(input('Введите высоту пирамиды: '))
for y in range(height):
    print(' ' * (height-y-1), end='')
    for x in range(y * 2 + 1):
        print('#', end='')
    print()