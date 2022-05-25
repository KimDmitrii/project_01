# Модуль работы с полем игры
# Copyright by Kim D.

from players import *
from help import MESSAGES, ANSWERS


# FIELD = [['']*3 for _ in range(3)]
FIELD = [['x', ' ', ' '], ['x', ' ', '0'], ['0', '0', '0']]
# создание поля для игры дз

# вывод поля на основе ходов в переменной FIELD
def show_field():
    print()
    print(*[' ', 0, 1, 2], '', sep=' | ')
    print('-'*15)
    for i,row in enumerate(FIELD):
        print([0, 1, 2][i], *row, '', sep=' | ')
        print('-'*15)

# проверка победы на основе сравнения данных FIELD с выигрышными комбинациями
def check_win():
    new_field = [n for row in FIELD for n in row]
    win_coordinates = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for win_coordinate in win_coordinates:
        if new_field[win_coordinate[0]] == new_field[win_coordinate[1]] == new_field[win_coordinate[2]] != ' ':
            break
            return True

# проверка наличия сохраненной партии
def check_saves(*, single=True):
    global PLAYER, FIELD
    # для парной игры
    s = set(PLAYER)
    # для одиночной игры
    if single:
        s |= {'ai1', 'ai2'}
    for save in SAVES:
        if set(save).issubset(s):
            # хочет ли игрок загрузить сохр партию
            load = input(MESSAGES[6]).lower()
            if load in ANSWERS[6]:
                FIELD = SAVES[save]
                return save
    return None

def game(load=False):
    # Цикл для одной партии
    while True:
        if load:
            # ход игрока сразу
            pass
        else:
            for player in PLAYER:
                if player.startswith('ai'):
                    # запрос хода бота
                    pass
                else:
                    # запрос хода игрока
                    pass

# ввод ходов будет через координаты же - по типу "введите две координаты от 0 до 2 через пробел" - это и будет ячейка в поле?
# загрузку игры буду копипастить у Вас, тк не знаю как ее делать, а завтра на работу.
# честно говоря эти функции я подглядел на гитхабе, но разобрался немного в них.

# при попытке запуска main в pycharm возникла ошибка NameError.
# Программа не видит PLAYER в field в check_save. скрин в тимс отправлю
# я немного поменял местами импорты в main и field, пытаясь решить эту проблему, но не помогло