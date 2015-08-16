def quick_sort(array):
    length = len(array)    
    q_sort(array, 0, length - 1)
    return array

def q_sort(array, start, end):
    pivot = start    
    left = start
    right = end    
    print "start %s end %s pivot %s " % (start, end, pivot)
    print array    
    if start == end:                
        return
    pivot_left = True
    total = end - start
    
    for i in range(total):        
        if pivot_left:
            if array[end] < array[start]:
               pivot_left = False
               array[end], array[start] = array[start], array[end]
               start += 1
               pivot = end
            else:
                end -= 1
        else:
            if array[start] > array[pivot]:
                pivot_left = True
                array[start], array[end] = array[end], array[start]
                end -= 1
                pivot = start
            else:
                start += 1        
    
    if left != pivot:
        # f = open("temp.txt", 'a')
        # f.write("left start %s end %s pivot %s " % (left, pivot - 1, pivot))
        # f.write(str(array))
        # f.close()
        q_sort(array, left, pivot -1)    
        
    if right != pivot:
        # f = open("temp.txt", 'a')
        # f.write("right start %s end %s pivot %s " % (pivot + 1, right, pivot))
        # f.write(str(array))
        # f.close()
        q_sort(array, pivot + 1, right)    
    
a = [4, 3, 15, 2, 9, 6, 20, 18]

print(quick_sort(a))

b = [10, 9, 8, 7, 6, 5, 3, 2, 1, -205]

print(quick_sort(b))

c = [1,2,3,4,5,6]

print(quick_sort(c))

d = [2,3,4,5,6,1]
d = [2,3,4,5,6,1]

print(quick_sort(d))