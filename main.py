# Модуль верхнего уровня приложения Крестики-Нолики
# Copyright by Gennadiy S. aka GennDALF

from players import *
from help import show_help, show_message

# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')



# запуск суперцикла
while True:
    command = input('_> ')

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break
    elif command in ('new', 'yes', 'новая', 'да'):
        # есть ли текущий игрок
        if not PLAYER:
            # запрос имени игрока
            player_name(PLAYER)
        else:
            game_mode = input('choose game mode(ai, human = ')
            if game_mode == 'ai':
                # Выбор уровня сложности
                difficult_lvl()
                PLAYER = PLAYER + (difficult_lvl(), )
                player_name(bot_mode=difficult_lvl())
                if all(k in SAVES for k in (PLAYER[0], PLAYER[1])):
                    print(f"Вам доступна сохраненная игра \n{PLAYER[0]} - {SAVES[PLAYER[0]]} \n{PLAYER[1]} - {SAVES[PLAYER[1]]}"
                        f"{input('Загрузить игру?(да/нет): ')}")
                else:
                    # далее проверка да/нет
                    # если да, то загружаем игру
                    # если нет, то переходим к выбору сложности
                    pass
                else:
                    # функция выбора символа
                    # старт партии
                    pass
            elif game_mode == 'human':
                player_name(PLAYER)
                if all(k in SAVES for k in (PLAYER[0], PLAYER[1])):
                    print(f"Вам доступна сохраненная игра \n{PLAYER[0]} - {SAVES[PLAYER[0]]} \n{PLAYER[1]} - {SAVES[PLAYER[1]]}"
                          f"{input('Загрузить игру?(да/нет): ')}")
                else:
                    mark = input('Выберите символ для первого игрока(x, 0): ')
                    # старт партии

# дописать скелет цикла
# функции игроков
# обработать запросы режима
# выбор сложности
# выбор символа
# все до старта партии и вывод статистики