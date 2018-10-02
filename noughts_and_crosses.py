"""Unbeatable game of nounts and crosses."""

import os
import random

points_used = []
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
box = "+--+"*3+"\n"+"|%s |"+"|%s |"+"|%s |"+"\n"+"+--+"*3


def _showboard():
    os.system("clear")
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


def _stalemate():
    print("its a draw")


def _checkforwin():
    for i in range(0, 3):
        if board[i] == ['x', 'x', 'x']:
            return True
        if board[i] == ['o', 'o', 'o']:
            return True
        stalemate = True
        for x in range(0, 3):
            for f in range(0, 3):
                if type(board[x][f]) == int():
                    stalemate = False
        if stalemate:
            _stalemate()
    if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            return True
    if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
            return True
    if board[0][-1] == 'x' and board[1][-1] == 'x' and board[2][-1] == 'x':
            return True
    if board[0][-1] == 'o' and board[1][-1] == 'o' and board[2][-1] == 'o':
            return True
    if board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
            return True
    if board[0][0] == 'o' and board[1][0] == 'o' and board[2][0] == 'o':
            return True
    if board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        return True
    if board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        return True
    if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        return True
    if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        return True
    return False


def _compturn():
    if len(points_used) == 0:
        points_used.append(random.choice([1,3,7,9]))
    num = random.randint(1, 10)
    if (num not in points_used) and (num < 10):
        points_used.append(num)
    else:
        _compturn()


def _dowin(val):
    print("\n" + val, "is the winner")
    exit()


cuser = ''
count = 0
win = False
while win is False:
    count += 1
    _showboard()
    if count % 2 == 0:
        cuser = 'x'
        _doboardchange(_userturn(), val='x')
    else:
        cuser = 'o'
        _compturn()
        _doboardchange(points_used[-1], val='o')
    win = _checkforwin()
_showboard()
_dowin(cuser)
