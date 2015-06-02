#!/usr/bin/env python
from numpy import *

class Matrix2D:    
    def __init__(self, dimension):
        #self.array = arange(dimension** 2).reshape(dimension, dimension)
        self.array = zeros((dimension, dimension),  dtype=int16)
        print("hello")
    
    def __str__(self):
      return str(self.array)
        
    def getSubArrayRow(self, row):
        return self.array[ row, : ]
    
    def getSubArrayColumn(self, col):
        return self.array[ : ,col]
    
    def getSubMatrix(self, startRow, startCol, height, width):
        return self.array[startRow:startRow + width:,startCol:startCol + height:]
        
    def addValue(self, row, col, value):
        self.array[row][col] = value    


### USAGE        
# matrix = Matrix2D(9)
# dimension = 9

# grids = """2 1 9 7 5 3 4 8 6
# 3 7 5 8 6 4 9 1 2
# 8 4 6 2 9 1 3 5 7
# 1 9 8 6 7 5 2 4 3
# 5 6 4 1 3 2 7 9 8
# 7 2 3 4 8 9 5 6 1
# 4 4 7 3 1 6 8 2 9
# 9 8 1 5 2 7 6 3 4
# 6 3 2 9 5 8 1 7 5"""

# grids = grids.split("\n")

# for i in range(0, 9):
#    inp = grids[i].split()    
#    for x in range(0, 9):
#        value = int(inp[x])
#        matrix.addValue(i, x, value)

# print(matrix)
# print(IsValid(matrix))
#print(matrix.getSubArrayColumn(3))
#print(matrix.getSubArrayRow(0))
#print(matrix.getSubMatrix(0,0,3,3))
#print(matrix.getSubMatrix(0,2,3,3))
#print(matrix.getSubMatrix(0,5,3,3))
