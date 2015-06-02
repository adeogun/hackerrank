#!/usr/bin/env python

class Matrix2D:  
    def __init__(self, dimension):
        #self.array = arange(dimension** 2).reshape(dimension, dimension)
        self.array =  [[0 for i in range(dimension)] for j in range(dimension)]
        self.dimension = dimension
    def __str__(self):
      return str(self.array)
        
    def getSubArrayRow(self, row):
        return self.array[row]
    
    def getSubArrayColumn(self, column):
        col = [None] * self.dimension
        count = 0
        for i in range(0, self.dimension):
            col[i] = self.array[i][column]
        return col
    
    def getSubMatrix(self, startRow, startCol, height, width):
        
        return  [[self.array[i][j] for j in range(startRow, startRow + height)] for i in range(startCol, startCol + width)]
    
    def addValue(self, row, col, value):
        self.array[row][col] = value    

    

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
