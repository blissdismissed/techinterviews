import math
import sys

class tictactoeboard:
    def addToken (self,currentstate, row,col,turn):
        if turn == 0:
            if row == 0: #0,3,6 positions
                if col == 0:
                    currentstate[0] = 'X'
                elif col == 1:
                    currentstate[1] = 'X'
                else: currentstate[2] = 'X'
            if row == 1: #1,4,7
                if col == 0:
                    currentstate[3] = 'X'
                elif col == 1:
                    currentstate[4] = 'X'
                else: currentstate[5] = 'X'
            if row == 2: #2,5,8
                if col == 0:
                    currentstate[6] = 'X'
                elif col == 1:
                    currentstate[7] = 'X'
                else: currentstate[8] = 'X'

        #boardstate = boardstate + #add next move using the row and col to calculate position in array
        return currentstate

    def printBoard (self, boardstate):
        for i in range(0,9,3):
            print(boardstate[i],"|",boardstate[i+1],"|",boardstate[i+2]) #0-4 for top row
        #     #print("|")
        # for i in range(4,6): #5-9 for top row
        #     print(boardstate[i])
        #     #print("|")
        # for i in range(7,9): #10-14 for top row
        #     print(boardstate[i])
        #     #print("|")

    def checkFull (self, boardstate):
        full = 0 # 0 is not full, 1 is full
        positionindex = 0
        for i in boardstate:
            if i == "-": 
                full = 0
                positionindex = index(i)
            else: full = 1
        return full

    

if __name__ == '__main__':
    startstate = ["-","-","-","-","-","-","-","-","-"]
    start = tictactoeboard()
    start.printBoard(startstate)
    print(" ")
    # player turn
    newstate = start.addToken(startstate,0,1,0)
    start.printBoard(newstate)
    print(checkFull(newstate))

