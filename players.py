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
    # не нужна переменная bot_mode
    bot = input('Выберите уровень сложности\n1 - легкий\n2 - трудный\n').lower()
    if bot in ('1', 'легкий', 'л'):
        return 'ai1'
    elif bot in ('2', 'трудный', 'т'):
        return 'ai2'
    else:
        # только вывод сообщения и всё?
        print('Вы ввели неверную команду')


# Кто ходит первым
def first_move():
    global PLAYER
    move = input(f"Каким символом желает играть игрок {PLAYER[0]}\n(X (ходит первым) или O)?\n").lower()
    if move == 'x':
        pass
    elif move == 'o':
        PLAYER = (PLAYER[1], PLAYER[0])
    else:
        # только вывод сообщения и всё?
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
        # после тире будет выведен список с вложенными списками – это то, чего вы хотите?
        print(f"Вам доступна сохраненная игра \n{PLAYER} - {SAVES[PLAYER]}")
        choice = input('Загрузить игру? ').lower()
        # лучше учесть несколько вариантов для положительного ответа
        if choice in ('yes', 'y', 'да', 'д'):
            # Загрузка игры
            pass
        # а для всех прочих реализовать вариант "нет"
        else:
            pass


# вывод статистики текущего(-их) игрока(-ов)
def show_stat():
    global PLAYER, PLAYERS
    # это для отладки?
    # просто не стоит переписывать глобальную переменную-кортеж вводом пользователя
    while PLAYER := input():
        if PLAYER in PLAYERS:
            print(f"Статистика побед, поражений и ничьих для - {PLAYER} - {PLAYERS[PLAYER]}")
        else:
            print(f" Для игрока {PLAYER} пока нет статистики побед, поражений и ничьих")
        PLAYER = tuple()
        print("Загрузить статистику другого игрока?(Нажмите Enter, если хотите выйти)")


# в целом – хорошая работа, так держать
