# Модуль верхнего уровня приложения Крестики-Нолики
# Copyright by Kim D.

from players import *
from help import show_help, show_message, MESSAGES, COMMANDS

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
        if mode():
            # продолжаем сохр партию
            # после завершения отобразить статистику
            show_stat(current=True)
            pass
        else:
            pass
            # начинаем новую
            # после завершения отобразить статистику
            show_stat(current=True)





