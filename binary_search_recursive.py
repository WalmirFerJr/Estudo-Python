def binarySearch(array_test, left, right, key):
    
    mid = (left + right) / 2
    mid = int(mid)

    if array_test[mid] == key:
        return mid
    elif left >= right:
        return -1
    elif key > array_test[mid]:
        return binarySearch(array_test, mid + 1, right, key)
    else:
        return binarySearch(array_test, left, mid - 1, key)
    
array_test = [10, 20, 30, 40, 50]
size_array = len(array_test)

print(binarySearch(array_test, 0, size_array - 1, 30))
        
