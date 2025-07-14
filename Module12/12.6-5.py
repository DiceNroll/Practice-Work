from random import randrange, choice


def rock_paper_scissors():
    actions = ['Камень', 'Ножницы', 'Бумага']
    pc_action = choice(actions)
    player_action = input('\nЧто ты выбрал?(к,н,б): ')
    # Ничья
    if pc_action == 'Камень' and player_action in 'Кк': print('Я выбрал', pc_action, 'у нас ничья!\n')
    if pc_action == 'Ножницы' and player_action in 'Нн': print('Я выбрал', pc_action, 'у нас ничья!\n')
    if pc_action == 'Бумага' and player_action in 'Бб': print('Я выбрал', pc_action, 'у нас ничья!\n')
    # Победа игрока
    if pc_action == 'Ножницы' and player_action in 'Кк': print('Я выбрал', pc_action, 'ты победил!\n')
    if pc_action == 'Бумага' and player_action in 'Нн': print('Я выбрал', pc_action, 'ты победил!\n')
    if pc_action == 'Камень' and player_action in 'Бб': print('Я выбрал', pc_action, 'ты победил!\n')
    # Победа пк
    if pc_action == 'Бумага' and player_action in 'Кк': print('Я выбрал', pc_action, 'я победил!\n')
    if pc_action == 'Камень' and player_action in 'Нн': print('Я выбрал', pc_action, 'я победил!\n')
    if pc_action == 'Ножницы' and player_action in 'Бб': print('Я выбрал', pc_action, 'я победил!\n')


def guess_the_number():
    if randrange(1, 11) == int(input('\nУгадайте число от 1 до 10: ')):
        print('Вы угадали!\n')
    else:
        print('К сожалению вы не угадали!\n')


def main_menu(act):
    if act == 1: rock_paper_scissors()
    if act == 2: guess_the_number()


while True:
    main_menu(int(input('1 - Камень, ножницы, бумага\n2 - Угадай число\nВыберете игру: ')))
