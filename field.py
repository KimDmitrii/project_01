# Модуль работы с полем игры

from shutil import get_terminal_size as gts
from itertools import chain

import players
import help
import ai

DIM = 3

FIELD = [['']*DIM for _ in range(DIM)]
# FIELD = [['x', '', 'o'], ['x', 'x', 'o'], ['', '', 'o']]
# символы
SYMBOLS = ('X', 'O')
# отладка
DEGUG = True

# вывод поля на основе ходов в переменной FIELD
def show_field(*, right=False): #center=False):

    # if center:
    #     FIELD = [[f'{i},{j}' for j in range(DIM)] for i in range(DIM)]
    # длина строки с максимальным количеством символов
    mx = max([len(cell) for row in FIELD for cell in row])
    wd = mx*DIM + DIM*3 - 1
    # отступ для выравнивания вывода слева, по центру или справа
    # margin = ' '*((gts()[0] - 1 - wd)//2) if center else ' '*(gts()[0] - 1 - wd) if right else ' '
    margin = ' '*(gts()[0] - 1 - wd) if right else ' '
    # формирование списка выводимых строк со значениями
    rows = [margin + '|'.join([cell.center(mx+2) for cell in row]) for row in FIELD]
    # вывод строк со значениями с горизонтальными линиями-разделителями
    print('\n' + ('\n' + margin + '—'*wd + '\n').join(rows) + '\n')
    # print(*rows. sep='\n' + margin + '-'*wd + '\n'

# проверка на победу или ничью
def check_win_or_tie():
    #  локальная функция: проверка на победу
    def check_win():
        # транспонированная матрица поля: для упрощения перебора
        #   столбцы прямой матрицы станут строками в транспонированной
        FIELD_T = [[FIELD[j][i] for j in range(DIM)] for i in range(DIM)]
        # список из главной и побочной диагоналей
        DIAGONALS = [[FIELD[i][i] for i in range(DIM)],
                     [FIELD[i][DIM - i - 1] for i in range(DIM)]]
        # перебираем прямую и транспонированные матрицы
        for matrix in (FIELD, FIELD_T, DIAGONALS):
            # есть ли ряд, целиком заполненный только одним символом
            if 1 in [len(set(row)) for row in matrix if all(row)]:
                # локаоьную функцию делали, чтобы не выполнять дальнейшие проверки
                #   как только будет найдена первая победная комбинация
                return True
    # нет пустых победа  ничья
    #   False    False   False
    #   False    True    False
    #   True     False   True
    #   True     True    False
    win = check_win()
    return win, all([all(row) for row in FIELD]) and not win

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

# функция партии, параметр load=False проверка загружаемой игры - да/нет
def game(load=False):
    global FIELD
    # одиночная False или партия True игра
    flag = set(players.PLAYER).isdisjoint({'ai1', 'ai2'})
    # флаг победы [0] или ничьи [1]
    win_or_tie = (False, False)
    # цикл для одной патрии
    while True:
        # перебираем игроков в кортеже
        for i in range(2):
            # Выбор приглашения для вводв
            prompt = ('ваш ход > ', f'ход игрока {players.PLAYER[i].title()} > ')[flag]
            # звпросить ход бота
            if players.PLAYER[i].startswith('ai'):
                # в случае загружаемой партии с ботом, когда игрок ходит ноликом (вторым)
                #   переключаем параметр load и переходим к следующей итерации
                #   цикла for (следующему ходу)
                if load and not i:
                    load = False
                    continue
                # проверяем уровень сложности
                y, x = ai.random_turn() if players.PLAYER[i][-1] == '1' else ai.ai_turn(i)
            # запросить ход игрока
            else:
                # в случае загружаемой игры с игроком, когда первый ход в возобновленной
                #   партии должен быть за вторым игроком, переключаем параметр load
                #   и переходим к следующей итерации цикла for (следующему ходу)
                if load and len([cell for row in FIELD for cell in row if cell]) % 2 != i:
                    load = False
                    continue
                # запрашиваем у игрока координаты пока он не укажет незанятую клетку
                while True:
                    y, x = map(int, input(prompt).split())
                    if not FIELD[y][x]:
                        break
            # обновляем матрицу поля
            FIELD[y][x] = SYMBOLS[i]
            # выводим поле с очередным ходом: слева или справа
            #   в зависимости от очередности хода
            show_field(right=bool(i))
            # проверяем, является ли данный ход завершающим
            win_or_tie = check_win_or_tie()
            # еще не закончили
            if not any(win_or_tie):
                continue
            # чья-то победа
            elif win_or_tie[0]:
                # сообщение о победе игрока
                help.show_message(f'Победил игрок {players.PLAYER[i]}!')
                # очищаем поле
                FIELD = [['']*3 for _ in range(DIM)]
                # ваня проиграл, олежа выйграл
                #   ({'ivan': [0, 1, 0]}, {'oleg': [1, 0, ]})
                return {players.PLAYER[i]: [0, 1, 0]}, {players.PLAYER[i-1]: [1, 0, 0]}
            # ничья
            elif win_or_tie[1]:
                # сообщение о ничьей
                help.show_message('Ничья!')
                # очищаем поле
                FIELD = [['']*3 for _ in range(DIM)]
                # у обоих ничья
                #   ({'ivan': [0, 0, 1]}, {'oleg': [0, 0, 1]})
                return {players.PLAYER[i]: [0, 0, 1]}, {players.PLAYER[i-1]: [0, 0, 1]}