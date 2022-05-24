# Модуль с данными игроков Крестики-Нолики
# Copyright by Kim S.

from configparser import ConfigParser

PLAYERS = {}
# PLAYERS = {'Ivan': [1,1,0], 'DIMA': [1,2,3], 'TANYA': [3,2,1]}
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


# Выбор уровня сложности
def difficult_lvl():
    bot_mode=''
    bot = input('Выберите уровень сложности(легкий/трудный) ').lower()
    if bot == 'легкий':
        bot_mode = 'ai1'
    elif bot == 'трудный':
        bot_mode = 'ai2'
    else:
        print('Вы ввели неверную команду')
    return bot_mode

# Кто ходит первым
def first_move():
    global PLAYER
    move = input(f"Каким символом желает играть игрок {PLAYER[0]}(X(ходит первым) или O)? ")
    if move == 'X':
        pass
    elif move == 'O':
        PLAYER = (PLAYER[1], PLAYER[0])
    else:
        print('Вы ввели неверный символ')

# запись имен в PLAYER
def player_name(bot_mode=''):
    global PLAYER
    # если имя игрока еще не вводилось
    if len(PLAYER) == 0:
        PLAYER = (input('Введите имя игрока ').lower(), )
    # если имя игрока уже вводилось
    elif len(PLAYER) == 1:
        if bot_mode:
            # добавить имя бота с уровнем сложности
            PLAYER = (PLAYER[0], bot_mode)
        else:
            # добавить имя второго игрока человека
            PLAYER = (PLAYER[0], input('Введите имя второго игрока ').lower())

# выбор режима игры
def mode():
    # зачем нужна переменная, которая используется один раз?
    return input('Выберите режим игры:\n1 - с ботом\n2 - двое игроков\n')

# загрузка сохраненной игры
def load_game():
    global PLAYER, SAVES
    if PLAYER in SAVES:
        print(f"Вам доступна сохраненная игра \n{PLAYER} - {SAVES[PLAYER]}")
        choice = input('Загрузить игру?(да/нет): ')
        if choice == 'да':
            # Загрузка игры
        elif choice == 'нет':
            pass

# вывод статистики текущего(-их) игрока(-ов)
def show_stat():
    global PLAYER, PLAYERS
    while PLAYER := input():
        if PLAYER in PLAYERS:
            print(f"Статистика побед, поражений и ничьих для - {PLAYER} - {PLAYERS[PLAYER]}")
        else:
            print(f" Для игрока {PLAYER} пока нет статистики побед, поражений и ничьих")
        PLAYER = tuple()
        print("Загрузить статистику другого игрока?(Нажмите Enter, если хотите выйти)")

