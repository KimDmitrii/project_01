# Модуль с данными игроков Крестики-Нолики
# Copyright by Kim S.

from field import *
from configparser import ConfigParser
from help import MESSAGES, ANSWERS, show_message


SCORES = {}
# PLAYERS = {'Ivan': [1,1,0], 'DIMA': [1,2,3], 'TANYA': [3,2,1]}
PLAYER = tuple()
SAVES = {}
# SAVES = {('ivan', 'ai1'): [[]],
#           ('ivan', 'oleg'): [[]]}


# Чтение data.ini
def read_ini():
    global SCORES, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        SCORES = {name: [int(n) for n in score.split(',')]
                  for name, score in config['Scores'].items()}
        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i+3]]
                      for i in range(0,9,3)]
                 for name, field in config['Saves'].items()}
        # первый запуск приложения
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileExistsError

# Запись в Data.ini
def save_ini():
    config = ConfigParser()
    config['Scores'] = {name: ','.join(str(n) for n in score)
                        for name, score in SCORES.items()}
    config['Saves'] = {';'.join(name):
                           ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config['Genera']['first'] = 'no'
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)


# запись имен в PLAYER
def player_name(bot_mode='', *, change_order=False):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input(MESSAGES[1]).lower(), )
    # если имя игрока уже вводилось
    elif len(PLAYER) == 1:
        if bot_mode:
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        else:
            # добавить имя второго игрока человека
            PLAYER = (PLAYER[0], input(MESSAGES[2]).lower())
    if change_order:
        PLAYER = (PLAYER[1], PLAYER[0])




# выбор режима игры
def mode():
    global PLAYER
    # запрос режима игры
    while True:
        gm = input(MESSAGES[3]).lower()
        if gm in ANSWERS[3]:
            break
    # если одиночная
    if gm in ANSWERS[3][:3]:
        # есть ли сохранение для одиночной игры
        if save := check_saves():
            # восстановление уровня сложности и очередности из SAVES
            PLAYER = save
            return True
        # запрос уровня сложности
        while True:
            dl = input(MESSAGES[4]).lower()
            if dl in ANSWERS[4]:
                break
        # запись имени бота
        if dl in ANSWERS[4][:3]:
            dl = 'ai1'
        else:
            dl = 'ai2'
        player_name(dl)
    # если парная
    else:
        player_name()
        if save := check_saves(single=False):
            # восстановление уровня сложности и очередности из SAVES
            PLAYER = save
            return True

    # выбор очередности хода
    if not (input(MESSAGES[5]).lower() in ANSWERS[5]):
        player_name(change_order=True)


# вывод статистики текущего(-их) игрока(-ов)
def show_stat(current=True):
    global PLAYER, SCORES
    # имя текущего игрока должно заводиться в PLAYERS сразу после ввода
    # а до ввода она просто не должна вызываться
    # это вариант отработки сразу после окончания партии
    if current:
        for p in PLAYER:
            if not p.startswith('ai'):
                print(f"Статистика побед, поражений и ничьих для - {p} - {SCORES[p]}")
    # это вариант для общей таблицы: первые десять результатов
    else:
        show_message('ТАБЛИЦА РЕЗУЛЬТАТОВ')
        print('\t\tпобед\tпоражений\tничьих')
        for p in sorted(SCORES.items(),
                        key=lambda pair: pair[1][0],
                        reverse=True)[:10]:
            print(f'{p[0]}\t{p[1][0]}\t{p[1][1]}\t{p[1][2]}')
    # что-то я увлёкся малость...)

# в целом – хорошая работа, так держать
