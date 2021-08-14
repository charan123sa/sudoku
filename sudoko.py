import random

def MakeSudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]
            
    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0
            
    # The range here is the amount
	# of numbers in the grid
    for i in range(5):
        #choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not CheckValid(Grid,row,col,num) or Grid[row][col] != 0): #if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        Grid[row][col]= num;
        
    Printgrid(Grid)

def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)
#     |-----------------------------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |-----------------------------|
    
def CheckValid(Grid,row,col,num):
    #check if in row
    valid = True
    #check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            #check if section is valid
            if(Grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid

MakeSudoku()