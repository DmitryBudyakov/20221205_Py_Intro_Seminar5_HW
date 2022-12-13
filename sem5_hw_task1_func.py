# Задача 1
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 117 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint


def get_choice() -> int:
    """ выбор по жребию 0 или 1
    0 - Player 1
    1 - Player 2
    """
    return randint(0, 1)


def player_action(remain_qty: int) -> int:
    """ действие игрока """
    limit_up = 28
    limit_down = 1
    while True:
        if remain_qty <= limit_up:
            taken = int(input(f'\nВзять можно не больше {remain_qty} конфет: '))
            if taken < limit_down or taken > remain_qty:
                print(f'Ошибка ввода. Повторите выбор.')
            else:
                break
        else:
            taken = int(input(f'\nВзять можно не больше {limit_up} конфет: '))
            if taken < limit_down or taken > limit_up:
                print(f'Ошибка ввода. Повторите выбор.')
            else:
                break
    return taken


def bot_action(remain_qty: int) -> int:
    """ действие бота """
    limit_up = 28
    limit_down = 1
    if remain_qty <= limit_up:
        taken = remain_qty
    else:
        taken = randint(limit_down, limit_up)
    return taken
