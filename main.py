# Модуль верхнего уровня приложения Крестики-Нолики
# Copyright by Kim D.

from players import *
from help import show_help, show_message

# приветствие
show_message('КРЕСТИКИ-НОЛИКИ')




# запуск суперцикла
while True:
    print('Введите команду:\nВыход из игры - "Выход" \nНовая игра - "Да"\n'
          'Показать статистику - "stat"')
    command = input('_> ').lower()

    if command in ('quit', 'выход'):
        # обработка завершения работы приложения
        break
    elif command in ('new', 'yes', 'новая', 'да'):
        # есть ли текущий игрок
        if not PLAYER:
            # Вводим имя первого игрока
            player_name()
        else:
            # выбор режима
            game_mode = mode()
            if game_mode in ('1', 'с ботом', 'бот'):

                # загружаем игру
                load_game()

                # выбор уровня сложности
                player_name(bot_mode=difficult_lvl())

                # функция выбора символа
                first_move()

                # старт партии

            elif game_mode in ('2', 'два игрока', 'двое'):

                # Вводим имя второго игрока
                player_name(bot_mode='')

                # предложение загрузить игру
                load_game()

                # функция выбора символа
                first_move()

                # старт партии

    elif command == 'stat':
        show_stat()


# в функции show_stat наверное надо делать ветвление if-else на фильтр по количеству побед
# для вывода статистики после партии нужно делать отдельную функцию?
# тк в этой происходит очистка переменной PLAYER, что возможно неправильно

# docstring убрал
