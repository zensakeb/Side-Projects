from typing import Dict
import numpy as np
import random

class CommonInteger:
    NEG_ONE = -1
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3

NUMBER_OF_ELEMENTS_PER_ROW_IN_A_BOX = CommonInteger.THREE

# single letter variable not allowed: dorkar hoile sentence lekhbi
# use of magic number detected: Google clean code and how to solve magic numbers
b = np.zeros(NUMBER_OF_ELEMENTS_PER_ROW_IN_A_BOX,int)
a = np.arange(1,4)
# box = np.array([a,a+3,a+6])

# try to come up with a bettr name for 'box'
box = np.array([b,b,b])
lines = np.array([box,box,box])
board = np.array([lines,lines,lines])
# board = np.array([[[[5,3,0],[6,0,0],[0,9,8]],[[0,7,0],[1,9,5],[0,0,0]],[[0,0,0],[0,0,0],[0,6,0]]],[[[8,0,0],[4,0,0],[7,0,0]],[[0,6,0],
#                 [8,0,3],[0,2,0]],[[0,0,3],[0,0,1],[0,0,6]]],[[[0,6,0],[0,0,0],[0,0,0]],[[0,0,0],[4,1,9],[0,8,0]],[[2,8,0],[0,0,5],[0,7,9]]]])

max_num_dict : Dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
max_num = []
win_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Python annotation: return type missing
def takeInput() -> None:

    # too many nested layers of loop... break into mutliple method/function
    z = 1
    for r in range(3):
        for c in range(3):
            i = 0
            input_box = [int(x) for x in input(f'Box-{z} : ').split()] # one of my favorite python syntax : list comprehension : +1 point
            z+= 1
            for x in range(3):
                for y in range(3):
                    board[r][c][x][y] = input_box[i]
                    i += 1

def max_num_sort():
    ax = dict(sorted(max_num_dict.items(), key=lambda x:x[1], reverse= True)) # na jaina code lekhar theika chaakri chaira dewa bhala : functional interface
    for k in ax.keys():
        max_num.append(k)

# method naming convention error
def printBoard():
    print()
    string = ''
    alp1 = ['X','Y','Z']
    alp_idx = 0
    for x in range(3):
        for y in range(1):
            string += "\n                            *----A----*----B----*----C----*"
            for z in range(3):
                if z == 1:
                    string += f"\n                          {alp1[alp_idx]} | {str(board[x][y][z])} | {str(board[x][y + 1][z])} | {str(board[x][y + 2][z])} | {alp1[alp_idx]}"
                    alp_idx += 1
                else:
                    string += f"\n                            | {str(board[x][y][z])} | {str(board[x][y + 1][z])} | {str(board[x][y + 2][z])} |"

    string += "\n                            *----A----*----B----*----C----*"


    print(string)

def randomPlay():
    for r in range(3):
        for c in range(3):
            for x in range(3):
                for y in range(3):
                    int_num = random.randrange(1, 10)

                    board[r][c][x][y] = int_num

    printBoard()

def crackPlay():

    takeInput()

    for r in range(3):
        for c in range(3):
            for x in range(3):
                for y in range(3):
                    a = board[r][c][x][y]
                    if a in max_num_dict.keys():
                        max_num_dict[a] += 1

    max_num_sort()
    print(max_num)
    recheck()
    # printBoard()

def recheck():
    while 0 in board:
        for key in max_num:
            if check(key) == True:
                pass

    print('***************************************** Your Crack *****************************************')
    print('                      Play the actual game! you Idiot')
    printBoard()

def check(key):

    for r in range(3):
        for c in range(3):
            if key in board[r][c]:
                for x in range(3):
                    if key in board[r][c][x]:
                        for y in range(3):
                            if board[r][c][x][y] == key:
                                crossBox(r, c, x, y)
                                break

    checkBox(key)
    resumeBox()
    return True

def crossBox(r,c,x,y):
    i,j,k,l = 0,0,0,0
    while j<3:
        while l<3:
            if board[r][j][x][l] == 0:
                board[r][j][x][l] = 10
            l +=1
        l = 0
        j += 1
    while i<3:
        while k<3:
            if board[i][c][k][y] == 0:
                board[i][c][k][y] = 10
            k += 1
        k=0
        i += 1

def resumeBox():
    r,c,x,y = 0,0,0,0
    while r<3:
        while c<3:
            while x<3:
                while y<3:
                    if board[r][c][x][y] == 10:
                        board[r][c][x][y] = 0
                    y+=1
                y = 0
                x+= 1
            x = 0
            c+= 1
        c = 0
        r+= 1

def checkBox(key):

    for r in range(3):
        for c in range(3):
            count = 0
            if key in board[r][c]:
                continue
            else:
                for x in range(3):
                    for y in range(3):
                        if board[r][c][x][y] == 0:
                            count += 1
            if count == 1:
                for x in range(3):
                    for y in range(3):
                        if board[r][c][x][y] == 0:
                            board[r][c][x][y] = key
            else:
                continue

#-------------------------------------------------------------------------------------------------------------------
while True:
    print()
    print()
    print('************************************Welcome to SuDoKu Crack-Play************************************')
    print()
    print('In the given box, put input as a whole sequence serial to the box.')
    print()
    print('****Remember to put space between your integers****')

    printBoard()

    print()

    crackPlay()