# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 07:35:54 2021

@author: asgin
"""

"""
Connect four, boardgame 
"""
def Winner(field,shape):
    for c in range(MAX_COULUMN-3):
        for r in range(MAX_ROW):
            if field[r][c] == shape and field[r][c+1] == shape and field[r][c+2] == shape and field[r][c+3] == shape:
                return True
    
    for c in range(MAX_COULUMN):
        for r in range(MAX_ROW-3):
            if field[r][c] == shape and field[r+1][c] == shape and field[r+2][c] == shape and field[r+3][c] == shape:
                return True

    for c in range(MAX_COULUMN-3):
        for r in range(MAX_ROW-3):
            if field[r][c] == shape and field[r+1][c+1] == shape and field[r+2][c+2] == shape and field[r+3][c+3] == shape:
                return True

    for c in range(MAX_COULUMN-3):
        for r in range(3,MAX_ROW):
            if field[r][c] == shape and field[r-1][c+1] == shape and field[r-2][c+2] == shape and field[r-3][c+3] == shape:
                return True

    

game = False
SHAPE_1 = "\u25C9"
SHAPE_2 = "\u03BF"
MAX_ROW = 7
MAX_COULUMN = 6

def Connect4(field):
    print("\n")
    # print("  1   2   3   4   5   6   7 ")
    # print("="*29)
    for row in range(12):
        fRow=int(row/2)
        if row%2 == 0:
            for column in range(15):
                if column%2 == 0:
                    fColumn=int(column/2)
                    if column != 14:
                        print("|" + field[fColumn][fRow], end = "")
                    else:
                        print("|")
                else:
                        print("", end = "")

        else:
            print("="*15)
            

player = 1
CurrentField=[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]
Connect4(CurrentField)     

while(game == False):
    try:        
        if player == 1:
            ChoseColumn = int(input("Player " + str(player) + " \u25C9 chose a ROW (1-7): "))-1
        else:
            ChoseColumn = int(input("Player " + str(player) + " \u03BF chose a ROW (1-7): "))-1
        if ChoseColumn >= 0 and ChoseColumn <= 6:
            # print(ChoseColumn)
            if player == 1:
                for i in range(5,-1,-1):
                    if CurrentField[ChoseColumn][i] == " ":
                        #print(ChoseColumn,i)
                        CurrentField[ChoseColumn][i] = "\u25C9" 
                        player=2
                        if Winner(CurrentField, SHAPE_1):
                            print("\n\n\u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9")
                            print("\u25C9 \u25C9 \u25C9 Player 1 Wins \u25C9 \u25C9 \u25C9")
                            print("\u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9 \u25C9")
                            game=True
                        
                        # print(CurrentField)
                        break
            else:
                for i in range(5,-1,-1):
                    if CurrentField[ChoseColumn][i] == " ":
                        #print(ChoseColumn,i)
                        CurrentField[ChoseColumn][i] = "\u03BF" #/u3007
                        player=1
                        
                        if Winner(CurrentField, SHAPE_2):
                            print("\n\n\u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF")
                            print("\u03BF \u03BF \u03BF Player 2 Wins \u03BF \u03BF \u03BF")
                            print("\u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF \u03BF")
                            game=True
                        # print(CurrentField)
                        break
        else:
            Connect4(CurrentField)
            print("ERROR: Out of range ( 1 - 7 )")

        Connect4(CurrentField)
        

    except Exception:
        Connect4(CurrentField)

        


        