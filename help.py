# Модуль работы со справкой приложения Крестики-Нолики
# Copyright by Gennadiy S. aka GennDALF

from shutil import get_terminal_size as gts
from math import floor, ceil

h = """Правила игры:
"""



def show_help():
    """Функция вывода справки"""
    print(h)

def show_message(text=''):
    width = gts()[0] - 1
    half_width = (width - len(text) - 2) / 2
    m = f"""{'#'*width}
{'#' + ' '*(width-2 + '#')}
{'#' + ' '*ceil(half_width) + text.upper() + ' '*floor(half_width) + '#'}
{'#' + ' '*(width-2 + '#')}
{'#'*width}"""
    print(m, end='\n\n')