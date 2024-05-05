import math

def median(arr):
    
    arr1 = arr
    arr1.sort()
    l = len(arr1)
    if l%2 == 1:
        return (arr1(l/2))
    
    else:
        f = arr1[math.floor(l/2)]
        c = arr1[math.ceil(l/2)]
        return ((f + c)/2)


arr = [11,2,3,4,7,6]
arr2 = [121,2,13,,3,4,7,6]

print(arr1)
print(median(arr1))
print(arr2)
