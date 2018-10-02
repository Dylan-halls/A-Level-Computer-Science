"""Unbeatable game of nounts and crosses."""

import os
import random

points_used = []
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
box = "+--+"*3+"\n"+"|%s |"+"|%s |"+"|%s |"+"\n"+"+--+"*3


def _showboard():
    for x in range(0, 3):
        points = ()
        for y in range(0, 3):
            points += (board[x][y],)
        print(box % points)


def _doboardchange(value, val=None):
    if val is not None:
        for i in board:
            try:
                i[i.index(value)] = val
            except ValueError:
                pass


def _userturn():
    num = int(input(">>> "))
    points_used.append(num)
    return num


def _checkforwin():
    val = 'x' or 'o'
    checkstr1 = (board[0][0] == val) and (board[0][1] == val) and (board[0][2] == val)
    checkstr2 = (board[0][0] == val) and (board[1][1] == val) and (board[2][2] == val)
    checkstr3 = (board[1][0] == val) and (board[1][1] == val) and (board[1][2] == val)
    checkstr4 = (board[2][0] == val) and (board[2][1] == val) and (board[2][2] == val)
    checkstr5 = (board[0][2] == val) and (board[1][1] == val) and (board[2][0] == val)
    checkstr6 = (board[0][2] == val) and (board[1][2] == val) and (board[2][2] == val)
    checkstr7 = (board[0][0] == val) and (board[1][0] == val) and (board[2][0] == val)
    # checkstr8 = (board[0][1] == val) and (board[0][1] == val) and (board[0][1] == val)
    return checkstr1 or checkstr2 or checkstr3 or checkstr4 or checkstr5 or checkstr6 or checkstr7


def _compturn():
    num = random.randint(1, 10)
    if (num not in points_used) and (num < 10):
        points_used.append(num)
    else:
        _compturn()


def _dowin(val):
    print("\n\n"+ val, "is the winner")
    exit()

count = 0
while True:
    count += 1
    os.system("clear")
    _showboard()
    win = _checkforwin()
    if win == False: pass
    elif win == True:
        if count % 2 == 0:
            print(_dowin('x'))
        else:
            print(_dowin('o'))
    if count % 2 == 0:
        _doboardchange(_userturn(), val='x')
    else:
        _compturn()
        _doboardchange(points_used[-1], val='o')
