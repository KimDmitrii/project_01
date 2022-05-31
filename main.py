# Модуль верхнего уровня приложения Крестики-Нолики
# Copyright by Kim D.

from players import PLAYER, mode, read_ini, show_stat, player_name
from help import COMMANDS, MESSAGES, show_help, show_message
from field import game

# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')

# куда делось чтение из файла?
if read_ini():
    show_help()

# запуск суперцикла
while True:

    command = input(MESSAGES[0]).lower()

    if command in COMMANDS['quit']:
        # обработка завершения работы приложения
        break

    elif command in COMMANDS['help']:
        show_help()

    elif command in COMMANDS['scores']:
        show_stat()

    elif command in COMMANDS['new']:
        # есть ли текущий игрок
        if not PLAYER:
            # Вводим имя первого игрока
            player_name()
        # запрос режимов игры
        if mode():
            # продолжаем сохраненную партию
            game(load=True)
            show_stat()
        else:
            # начинаем новую партию
            game()
            # show_stat()





