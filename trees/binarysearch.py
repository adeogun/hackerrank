class binarysearch:
    
    def __init__(self, array):
        self.array = array
        self.array.sort()        
        
    def searchRecursive(self, target, array):                
        if len(array) == 0:
            self.index = None
            return False        
            
        if len(array) % 2 == 0:
            mid = (len(array) // 2) - 1
        else:
            mid = (len(array) // 2)
            
        if target > array[mid]:            
            return self.searchRecursive(target, array[mid + 1:])
        if target < array[mid]:            
            return self.searchRecursive(target, array[:mid])
        if target == array[mid]:
            return True
    
    def searchRecuriveIndex(self, target, indexl, indexr, array):
        
        diff = indexr - indexl        
            
        if diff == 1:
            if array[indexr] == target:
                return (indexr, target)
            if array[indexl] == target:
                return (indexl, target)            
            return None
        
        if diff % 2 == 0:
            mid = (diff // 2 ) +  indexl 
        else:
            mid = (diff // 2) + 1 + indexl                     
        
        if mid > len(array) - 1:
            return None       
        
        if target > array[mid] and indexl != indexr:             
            return self.searchRecuriveIndex(target, mid + 1, indexr, array)
        if target < array[mid] and indexl != indexr:            
            return self.searchRecuriveIndex(target, indexl,  mid - 1 , array)
        if target == array[mid]:
            return (mid, array[mid])
        if indexl == indexr:
            return None
        
    def searchExists(self, target):                
        return self.searchRecursive(target, self.array)
    
        
    def searchIndex(self, target):        
        return self.searchRecuriveIndex(target, 0, len(self.array) - 1, self.array)
        

    #b = binarysearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

#
#print(b.searchExists(1))
#print(b.searchExists(2))
#print(b.searchExists(5))
#print(b.searchExists(13))
#print(b.searchExists(14))
#print(b.searchExists(100))
#print(b.searchExists(-1))
#print("----------------")
#
#for i in range(15):
#    print(b.searchIndex(i))
#print(b.searchIndex(-100))
#print(b.searchIndex(-1))
#print(b.searchIndex(100))

#b = binarysearch([1,2,3,4,6,7,9,10,11,12,14])
#for i in range(15):
#    print(b.searchIndex(i))
