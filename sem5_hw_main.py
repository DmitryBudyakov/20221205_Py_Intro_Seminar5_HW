# Задача 1
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 117 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

from sem5_hw_task1_func import *
import os

def clear_screen():
    """ очистка экрана """
    if os.name == 'nt':
        os.system('cls')
    else:
        clr_screen = os.system('clear')

def show_head():
    """ шапка игры """
    title = 'Игра с конфетами'
    sub_title1 = f'За один ход можно забрать не более чем {limit_up} конфет.'
    sub_title2 = 'Побеждает тот, кто сделает последний ход.'
    print('-'*len(sub_title1))
    print(' '*((len(sub_title1)-len(title))//2), title)
    print(sub_title1)
    print(sub_title2)
    print('-'*len(sub_title1))

    
def game_menu() -> str:
    """ меню игры """
    head_menu = \
"Меню игры\n\
----------\n\
Выберите режим игры:\n\
1) Игра с человеком\n\
2) Игра с ботом\n\
q) Выйти\n"
    choice = "Выберите [1, 2, q]: "
    initial_menu = head_menu + choice
    answers = ['1', '2', 'q']
    while True:
        selector = input(initial_menu)
        if selector not in answers:
            error_msg = 'Ошибка ввода. Повторите выбор.\n'
            initial_menu = head_menu + error_msg + choice
            clear_screen()
            show_head()
        elif selector == 'q':
            # print('Bye-bye!')
            print(msg_on_exit)
            exit()
        else:
            clear_screen()
            show_head()
            return selector

def game_repeat():
    """ запрос на повтор игры """
    answers = ['yes', 'y', 'no', 'n']
    while True:
        answer = input('Повторить игру? [yes, no]: ')
        if answer not in answers:
            print("Выберите 'yes' или 'no'")
        elif answer == 'no' or answer == 'n':
            # print('Bye-bye!')
            print(msg_on_exit)
            exit()
        elif answer == 'yes' or answer == 'y':
            game_init()
            game_play()


def game_init():
    """ инициализация параметров игры """
    global total_qty, turn, sel
    total_qty = 117
    turn = get_choice() # определение 1-го хода: 0 - player 1,  1 - player 2
    clear_screen()      # очистка экрана
    show_head()         # шапка игры
    sel = game_menu()   # выбор режима игры 1 - с человеком, 2 - с ботом

    
def game_play():
    """ логика игры """
    global total_qty, turn, sel
    while total_qty > 0:
        if turn == 1 and sel == '2':
            player = 'Player 2(бот)'
        elif turn == 1:
            player = 'Player 2'
        else:
            player = 'Player 1'
        print(f'Осталось: {total_qty} конфет')    
        print(f'Ход: {player}')
        if turn == 0 or sel == '1':
            total_qty -= player_action(total_qty)
        elif turn == 1 and sel == '2':
            bot_taken = bot_action(total_qty)
            total_qty -= bot_taken
            print(f'\n{player} взял {bot_taken} конфет. Нажмите [Enter] ', end='')
            input()
        if total_qty <= 0:
            print(f'\nИгра окончена. Выиграл {player}. Поздравляем победителя!')
            game_repeat()
        else:
            if turn == 0:
                turn = 1
            else:
                turn = 0
            clear_screen()
            show_head()

  
global msg_on_exit, limit_up
msg_on_exit = '\nВыход из игры. Пока-пока!'
limit_up = 28

game_init()     # начальные параметры: кол-во конфет, чей ход, вариант игры
game_play()     # логика игры
