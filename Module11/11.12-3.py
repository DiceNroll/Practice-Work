size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова ваша скорость соединения: '))
sec = 0
while speed * sec < size - speed:
    sec += 1
    print('Прошло', sec, 'сек.', 'Скачано', speed * sec, 'из', size, 'Мб', '(' + str(round(sec * speed / size * 100)) + '%)')
print('Прошло', sec + 1, 'сек.', 'Скачано', size, 'из', size, 'Мб (100%)')
