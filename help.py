# Модуль работы со справкой приложения Крестики-Нолики
# Copyright by Kim D.

from shutil import get_terminal_size as gts
from math import floor, ceil

h = """Правила игры:
"""


def show_help():
    """Функция вывода справки"""
    # а вы знаете, что это 🡼 за строка и почему она здесь?
    print(h)

# описать функцию: что она делает?
def show_message(text=''):
    width = gts()[0] - 1
    half_width = (width - len(text) - 2) / 2
    # можно ещё вот так определить строку
    # неявной конкатенаций строк внутри явного выражения в скобках
    m = (f"\n{'#' * width}"
         f"\n{'#' + ' ' * (width - 2) + '#'}"
         f"\n{'#' + ' ' * ceil(half_width) + text.upper() + ' ' * floor(half_width) + '#'}"
         f"\n{'#' + ' ' * (width - 2) + '#'}"
         f"\n{'#' * width}")
    print(m, end='\n\n')
