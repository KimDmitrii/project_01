# импорты
from configparser import ConfigParser


# глобальные переменные
FIELD = [['']*3 for _ in range(3)]
PLAYERS = {'Ivan': [1,1,0]}
# PLAYERS = {'Ivan': [1,1,0]}
SAVES = {}
# SAVES = {('ivan', 'ai1'): [[]]}

# функции

# подписывайте, что делает эта функция
def field():
    global FIELD
    pass

# подписывайте, что делает эта функция
def show_help():
    pass

# подписывайте, что делает эта функция
def read():
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

# подписывайте, что делает эта функция
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


# чтение .ini файла
if read():
    show_help()

# запуск суперцикла
while True:
    command = input()

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break

    # ввод имени игрока


# commit messages должны быть:
#   а) краткими
#   б) на естественном языке
#   в) без кода или псевдокода
# также, в них можно писать на русском

# вот это сообщение
    # add functions:
    # read() - read data.ini (name: score from PLAYERS, name: field from SAVES)
    #
    # save() - save data.ini (name: score in PLAYERS,
    # name: field in SAVES)
    # when save then ['Genera']['first'] = 'no'

# следует переписать
    # функции read, save для data.ini

# в commit message этого достаточно
