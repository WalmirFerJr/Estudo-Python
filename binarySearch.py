def binarySearch(array_test, left, right, key):
    
    while left <= right:
        mid = (left + right) / 2

        if array_test(mid) == key:
            return array_test(mid)
        
        elif:
