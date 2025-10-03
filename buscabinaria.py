def binarySearch(number_list, left, right, key):

    while left <= right:
        mid = (left + right) / 2

        if key == mid:
            return number_list[mid]

        elif key > mid:
            binarySearch(number_list, (mid + 1), right, key)

        else:
            binarySearch(number_list, left, (mid - 1), key)

    return (-1)

number_list = [10, 20, 30, 40, 50]
lenght = len(number_list)

binarySearch(number_list, 0, (lenght - 1), 20)