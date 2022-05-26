# Модуль работы с полем игры
# Copyright by Kim D.

import players
import help


# FIELD = [['']*3 for _ in range(3)]
FIELD = [['x', ' ', ' '], ['x', ' ', '0'], ['0', '0', '0']]
# создание поля для игры дз

# вывод поля на основе ходов в переменной FIELD
def show_field(indexed=False):
    print()
    # поле будет выводиться после каждого хода, то есть довольно часто
    #   а значит, номера строк и столбцов будут явно лишними,
    #   но можно их выводить только в определённой ситуации,
    #   например во время объяснения правил
    if indexed:
        print(*[' ', 0, 1, 2], '', sep=' | ')
        # в зависимости от наличия столбца с номерами строк, у нас будет меняться
        #   количество символов для горизонтальной линии-разделителя строк
        line = ' ' + '—'*17
    else:
        line = ' ' + '—'*13
    print(line)
    for i, row in enumerate(FIELD):
        if indexed:
            # что это было? обращаться к элементу списка по индексу, который равен элементу...
            print('', i, *row, '', sep=' | ')
        else:
            print('', *row, '', sep=' | ')
        print(line)

# проверка победы на основе сравнения данных FIELD с выигрышными комбинациями
def check_win():
    new_field = [n for row in FIELD for n in row]
    win_coordinates = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for win_coordinate in win_coordinates:
        if new_field[win_coordinate[0]] == new_field[win_coordinate[1]] == new_field[win_coordinate[2]] != '':
            # break прерывает цикл,
            #   а return прерывает цикл, завершает работу функции
            #   и возвращает переданное значение
            return True

# проверка наличия сохраненной партии
def check_saves(*, single=True):
    # мы не пытаемся здесь изменить переменную PLAYER,
    #   поэтому не нужно её добавлять в global
    global FIELD
    # для парной игры
    s = set(players.PLAYER)
    # для одиночной игры
    if single:
        s |= {'ai1', 'ai2'}
    for save in players.SAVES:
        if set(save).issubset(s):
            # хочет ли игрок загрузить сохр партию
            load = input(help.MESSAGES[6]).lower()
            if load in help.ANSWERS[6]:
                FIELD = players.SAVES[save]
                return save
    return None

# что это за функция? что значит параметр load?
def game(load=False):
    # Цикл для одной партии
    while True:
        if load:
            # ход игрока сразу
            pass
        else:
            for player in players.PLAYER:
                if player.startswith('ai'):
                    # запрос хода бота
                    pass
                else:
                    # запрос хода игрока
                    pass

# ввод ходов будет через координаты же -
# по типу "введите две координаты от 0 до 2 через пробел" -
# это и будет ячейка в поле?
#       да

# загрузку игры буду копипастить у Вас, тк не знаю как ее делать, а завтра на работу.
# честно говоря эти функции я подглядел на гитхабе, но разобрался немного в них.
#       не разобрались, к сожалению

# при попытке запуска main в pycharm возникла ошибка NameError.
# Программа не видит PLAYER в field в check_save. скрин в тимс отправлю
# я немного поменял местами импорты в main и field, пытаясь решить эту проблему, но не помогло
#       отлично! вы столкнулись с так называемым циклическим импортом
#       здесь исправлю код на верный, а подробно объясню на занятии
