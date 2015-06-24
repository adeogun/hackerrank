import math

def triangle(n):
    return n * (n + 1)
    
def nextPermutation(array):
    tail = len(array) - 1
    while tail > 0 and array[tail - 1] >= array[tail]:
        tail -=  1        
    
    if tail <= 0:
        return False    
    
    i = len(array) - 1
    while array[i] <= array[tail - 1]:
        i -= 1         
    b = array[tail - 1]
    array[tail - 1] = array[i]
    array[i] = b
    
        
    b = array[:tail]
    c = array[tail:]
    c.reverse()
    return  b + c

print(nextPermutation([0, 1, 2,  5, 3, 3, 0 ]))