def binarySearch(number_list, left, right, key):

    while left <= right:
        mid = (left + right) / 2
        mid = int(mid)
    
        if number_list[mid] == key:
            return mid
        elif key > number_list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return (-1)

number_list = [10, 20, 30, 40, 50]
lenght = len(number_list)

print(binarySearch(number_list, 0, lenght - 1, 40))