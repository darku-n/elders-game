from random import randint
from sys import platform
from time import sleep
import os

rowline_value = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
gameover = False

def build_game(rl):
    for c in range(0, 3):
        print(rl[c][0] + ' | ' + rl[c][1] + ' | ' + rl[c][2])
        if c != 2:
            print('--+---+--')

def pc_play():
    global rowline_value
    global pc_choice
    print('Vez do computador:')
    print()
    while True:
        inserted = False
        computer_play = randint(1, 9)
        for c in range(0,3):
                if str(computer_play) in rowline_value[c]:
                    rowline_value[c][rowline_value[c].index(str(computer_play))] = pc_choice
                    inserted = True
        if inserted == True:
            break

def gameover_check(rl):
    global gameover
    global n_moves
    for c in range(0, 3):
        if rl[c][0] == rl[c][1] == rl[c][2]:
            gameover = True
        elif rl[0][c] == rl[1][c] == rl[2][c]:
            gameover = True
        if c == 0:
            if rl[0][0] == rl[1][1] == rl[2][2]:
                gameover = True
            elif rl[0][2] == rl[1][1] == rl[2][0]:
                gameover = True
    
    if n_moves >= 9:
        gameover = True
    if gameover == True:
        print()
        print('='*30)
        print('         Fim de jogo!')
        print('='*30)

def clear_screen():
    sleep(0.5)
    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')

char_choice = int(input(''' Você quer X ou O?
[1] X
[2] ⬤
> '''))
if char_choice == 1:
    char_choice = 'X'
    pc_choice = '⬤'
else:
    char_choice = '⬤'
    pc_choice = 'X'
start_player = randint(0, 10)
n_moves = 0
clear_screen()
print()

while True:
    if start_player < 6:
        clear_screen()
        if n_moves == 0:
            print('O computador inicia o jogo')
        pc_play()
    else:
        clear_screen()
        if n_moves == 0:
            print('Você inicia o jogo')
            print()
        start_player = 0

    build_game(rowline_value)
    n_moves += 1
    print()
    print('-'*30)
    print()

    gameover_check(rowline_value)
    sleep(1)
    if gameover == True:
        break

    userinput = 0
    while True:
        inserted = False
        userinput = int(input('''Selecione a casa que deseja jogar(1-9): 
> '''))
        if not 1 <= userinput <= 9:
            print('Casa inválida!')
        else:
            for c in range(0,3):
                if str(userinput) in rowline_value[c]:
                    rowline_value[c][rowline_value[c].index(str(userinput))] = char_choice
                    inserted = True
            if inserted == True:
                break
            else:
                print('Casa inválida!')
    
    clear_screen()
    print('Sua jogada:')
    print()
    build_game(rowline_value)
    n_moves += 1
    sleep(1)
    gameover_check(rowline_value)
    if gameover == True:
        break
    print()
    print('-'*30)
    print()
