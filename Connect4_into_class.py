from typing import Callable
import csv


class Connectfour():
    def __init__(self):
        self.grid = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
        ]

    def place_oneBlue(self, grid: list[list[int]], col: int) -> bool:
         """Attempts to place a 1 in the lowest available 0 in the given column. Returns True if successful, False if the column is full."""
         with open('Block 3/grid.csv', "r+",newline='') as self.grids:
            self.csv_grid = csv.writer(self.grids)
            self.grid = grid
            self.col = col

            self.Flag = False
            for self.i in range(len(self.grid) - 1, -1, -1):
                if self.grid[self.i][self.col] == 0:
                    self.grid[self.i][self.col] = 1
                    self.Flag = True
                    for self.line in self.grid:
                        self.csv_grid.writerow(self.line)
                        print(self.line)
                    break
         if self.Flag == False:
            print(f"Column {col} is full. No placement possible.")
         return self.Flag
        

    def place_oneRed(self, grid: list[list[int]], col: int) -> bool:
        """Attempts to place a 1 in the lowest available 0 in the given column. Returns True if successful, False if the column is full."""
        with open('Block 3/grid.csv', "r+",newline='') as self.grids:
            self.csv_grid = csv.writer(self.grids)
            self.grid = grid
            self.Flag = False
            self.col = col
            for self.i in range(len(self.grid) - 1, -1, -1):
                if self.grid[self.i][self.col] == 0:
                    self.grid[self.i][self.col] = -1
                    self.Flag = True
                    for self.line in self.grid:
                        self.csv_grid.writerow(self.line)
                        print(self.line)
                    break
        if self.Flag == False:
            print(f"Column {col} is full. No placement possible.")
        return self.Flag
        
    def userChoice(self, userinput, call:Callable):
        self.userinput = userinput
        self.call = call
        print("Player Blue Turn")
        if self.userinput == 99:
            exit()
        self.calling = self.call(self.grid, self.userinput)
        return self.calling          #not returning false or true
    
    def checkwinHorizonal(self):
        with open('Block 3/grid.csv', "r",newline='') as self.output:
            self.countBlue = 0
            self.countRed = 0
            self.csv_reader = csv.reader(self.output)
            for self.line in self.csv_reader:
                for self.num in self.line:
                    if self.num == '1':
                        self.countBlue += 1
                        if self.countBlue == 4:
                            print("Blue winner!")
                            exit()
                            break
                    else:
                        self.countBlue = 0
                    if self.num == '-1':
                        self.countRed += 1
                        if self.countRed == 4:
                            print("Red is the winner!")
                            exit()
                            break
                    else: 
                        self.countRed = 0

    def checkwinVertical(self, gridT):
        self.gridT = gridT
        self.gridT = self.grid
        self.transposed_matrix = []
        for self.row in zip(*self.gridT):
            self.transposed_matrix.append(list(self.row))
        for self.line in self.transposed_matrix:
            for self.num in self.line:  #fix
                if str(self.num) == '1':
                    self.countBlue += 1
                    if self.countBlue == 4:
                        print("Blue winner!")
                        exit()
                        break
                else:
                    self.countBlue = 0
                if str(self.num) == '-1':
                    self.countRed += 1
                    if self.countRed == 4:
                        print("Red is the winner!")
                        exit()
                        break
                else: 
                    self.countRed = 0

    def check_diagonalsBlue(self, grid):
        self.grid = self.grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        
        for self.row in range(self.rows - 3):  # avoid index out of bounds
            for self.col in range(self.cols - 3):
                self.val = self.grid[self.row][self.col]
                if self.val != 0 and self.val == self.grid[self.row+1][self.col+1] == self.grid[self.row+2][self.col+2] == self.grid[self.row+3][self.col+3]:
                    print("Blue is the winner!")
                    exit()

        for self.row in range(3, self.rows):  # start from row 3 to avoid going out of bounds upward
            for self.col in range(self.cols - 3):
                self.val = self.grid[self.row][self.col]
                if self.val != 0 and self.val == grid[self.row-1][self.col+1] == grid[self.row-2][self.col+2] == grid[self.row-3][self.col+3]:
                    print("Blue is the winner!")
                    exit()

    def check_diagonalsRed(self, grid):
        self.grid = self.grid
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        
        for self.row in range(self.rows - 3):  # avoid index out of bounds
            for self.col in range(self.cols - 3):
                self.val = self.grid[self.row][self.col]
                if self.val != 0 and self.val == self.grid[self.row+1][self.col+1] == self.grid[self.row+2][self.col+2] == self.grid[self.row+3][self.col+3]:
                    print("Blue is the winner!")
                    exit()

        for self.row in range(3, self.rows):  # start from row 3 to avoid going out of bounds upward
            for self.col in range(self.cols - 3):
                self.val = self.grid[self.row][self.col]
                if self.val != 0 and self.val == self.grid[self.row-1][self.col+1] == grid[self.row-2][self.col+2] == grid[self.row-3][self.col+3]:
                    print("Blue is the winner!")
                    exit()
        
    def runGames(self):
        self.run = True
        while self.run == True:
            self.CurPlayer = 1
            if self.CurPlayer == 1:
                print("Player Blue Turn")
                self.userinput = int(input("What row are you choosing from? 0 - 7: "))
                self.worked = self.userChoice(self.userinput, self.place_oneBlue)
                if self.worked == True:
                    self.CurPlayer = 0
                else:
                    self.CurPlayer = 1
                self.checkwinHorizonal()
                self.checkwinVertical(self.grid)
                self.check_diagonalsBlue(self.grid)

            if self.CurPlayer == 0:
                print("Player Red Turn")
                self.userinput = int(input("What row are you choosing from? 0 - 7: "))
                self.worked = self.userChoice(self.userinput, self.place_oneRed)
                if self.worked == True:
                    self.CurPlayer = 1
                else:
                    self.CurPlayer = 0
                self.checkwinHorizonal()
                self.checkwinVertical(self.grid)
                self.check_diagonalsRed(self.grid)

if __name__ == "__main__":
    Connectfour().runGames()