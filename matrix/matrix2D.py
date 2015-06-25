#!/usr/bin/env python

class Matrix2D:  
    def __init__(self, dimension):
        #self.array = arange(dimension** 2).reshape(dimension, dimension)
        self.array =  [[0 for i in range(dimension)] for j in range(dimension)]
        self.dimension = dimension
    def __str__(self):
      return str(self.array)
        
    def get_sub_array_row(self, row):
        return self.array[row]
    
    def get_sub_array_column(self, column):
        col = [None] * self.dimension
        count = 0
        for i in range(self.dimension):
            col[i] = self.array[i][column]
        return col
    
    def get_sub_matrix(self, startRow, startCol, height, width):
        return  [[self.array[i][j] for j in range(startRow, startRow + height)] for i in range(startCol, startCol + width)]
    
    def add_value(self, row, col, value):
        self.array[row][col] = value    

    def get_diagonal_right(self):
        right = [None] * self.dimension
        for i in range(self.dimension):
            right[i] = self.array[i][self.dimension - i -1 ]
        
        return right
    
    def get_diagonal_left(self):
        left = [None] * self.dimension
        for i in range(self.dimension):
            left[i] = self.array[i][i]
            
        return left

### USAGE        
#matrix = Matrix2D(9)
#dimension = 9
#
#grids = """2 1 9 7 5 3 4 8 6
#3 7 5 8 6 4 9 1 2
#8 4 6 2 9 1 3 5 7
#1 9 8 6 7 5 2 4 3
#5 6 4 1 3 2 7 9 8
#7 2 3 4 8 9 5 6 1
#4 4 7 3 1 6 8 2 9
#9 8 1 5 2 7 6 3 4
#6 3 2 9 5 8 1 7 5"""
#
#grids = grids.split("\n")
#
#for i in range(0, 9):
#   inp = grids[i].split()    
#   for x in range(0, 9):
#       value = int(inp[x])
#       matrix.addValue(i, x, value)
#
#print(matrix)
#print()
#print(matrix.getSubArrayColumn(3))
#print()
#print(matrix.getSubArrayRow(0))
#print()
#print(matrix.getSubMatrix(0,0,3,3))
#print()
#print(matrix.getSubMatrix(0,2,3,3))
#print()
#print(matrix.getSubMatrix(0,5,3,3))
#print(matrix.getDiagonalLeft())
#print(matrix.getDiagonalRight())