for y in range(11):
    for x in range(31):
        if x == 0 or x == 30:
            print('|', end='')
        elif y == 0 or y == 10:
            print('-', end='')
        else:
            print(' ', end='')
    print()
