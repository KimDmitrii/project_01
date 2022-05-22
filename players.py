# Модуль с данными игроков Крестики-Нолики
# Copyright by Gennadiy S. aka GennDALF
from configparser import ConfigParser

PLAYERS = {}
# PLAYERS = {'Ivan': [1,1,0]}

PLAYER = tuple()
SAVES = {}
# SAVES = {('ivan', 'ai1'): [[]],
#           ('ivan', 'oleg'): [[]]}

# Чтение data.ini
def read_ini():
    global PLAYERS, SAVES
    config = ConfigParser()
    if config.read('data.ini', encoding='utf-8'):
        PLAYERS = {name: [int(n) for n in score.split(',')]
                   for name, score in config['Scores'].items()}
        SAVES = {tuple(name.split(';')):
                     [[' ' if c == '-' else c for c in field[i:i+3]]
                      for i in range(0,9,3)]
                 for name, field in config['Saves'].items()}
        return True if config['General']['first'] == 'yes' else False
    else:
        raise FileExistsError

# Запись в Data.ini
def save():
    config = ConfigParser()
    config['Scores'] = {name: ','.join(str(n) for n in score)
                        for name, score in PLAYERS.items()}
    config['Saves'] = {';'.join(name):
                           ''.join(['-' if c == ' ' else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config['Genera']['first'] = 'no'
    with open('data.ini', 'w', encoding='utf-8') as config_file:
        config.write(config_file)

 # Выборо уровня сложности
def difficult_lvl():
    bot = input('Выберите бота(ai1, ai2): ')
    return bot

# Кто ходит первым
def firstMove():
    # Здесь будет логика выбора первого хода
    # далее использовать эту функцию в функции player_name() в последнем блоке else(строка 62),
    # только я не знаю как

# запись имен в PLAYER
def player_name(bot_mode=''):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input().lower(), )
    # если имя игрока еще вводилось
    elif len(PLAYER) == 1:
        if bot_mode:
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        else:
            # добавить имя второго игрока человека
            PLAYER = (PLAYER[0], input().lower())
    else:



