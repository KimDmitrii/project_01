# Модуль работы со справкой приложения Крестики-Нолики
# Copyright by Kim D.

from shutil import get_terminal_size as gts
from math import floor, ceil

h = """Правила игры:
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
