def letter_count(text, num, let):
    print('\nКоличество цифр '+num+':', [i for i in text].count(k))
    print('Количество букв '+let+':', [i for i in text].count(n))


text = input('Введите текст: ')
num = input('Какую цифру найти: ')
let = input('Какую букву найти: ')
letter_count(text, num, let)
