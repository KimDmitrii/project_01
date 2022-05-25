# Модуль работы со справкой приложения Крестики-Нолики
# Copyright by Kim D.

from shutil import get_terminal_size as gts
from math import floor, ceil


MESSAGES = ('хотите начать новую партию? >',
            'введите имя игрока >',
            'введите имя второго игрока >',
            'выберите режим игры:\n 1 - с ботом\n 2 - с человеком\n>',
            'выберите уровень сложности игры:\n 1 - легкий\n 2 - трудный\n>',
            'Вы хотите ходить первым? >',
            'Вы хотите загрузить сохраненную партию ? >'
            )

COMMANDS = {'quit': ('quit', 'выход'),
            'help': ('help', 'помощь', 'h', '?'),
            'scores': ('stat', 'таблица', 'статистика', 'rating', 'рейтинг'),
            'new': ('new', 'yes', 'новая', 'да')}

ANSWERS = (None,
           None,
           None,
           ('1', 'бот', 'б', '2', 'человек', 'ч'),
           ('1', 'легкий', 'л', 'трудный', '2', 'т'),
           ('yes', 'да', 'y', 'д'),
           ('yes', 'да', 'y', 'д')
           )

h = f"""Правила игры:
Список команд:
{' '.join(COMMANDS['quit'])}
"""



# вывод справки
def show_help():
    print(h)

# вывод приветствия
def show_message(text=''):
    width = gts()[0] - 1
    half_width = (width - len(text) - 2) / 2
    m = (f"\n{'#' * width}"
         f"\n{'#' + ' ' * (width - 2) + '#'}"
         f"\n{'#' + ' ' * ceil(half_width) + text.upper() + ' ' * floor(half_width) + '#'}"
         f"\n{'#' + ' ' * (width - 2) + '#'}"
         f"\n{'#' * width}")
    print(m, end='\n\n')
