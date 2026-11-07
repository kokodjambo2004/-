from bisect import bisect_left


def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


values = [3, 39, 40, 58, 67, 83, 89, 97, 113, 128]
target = 40

position = binary_search(values, target)
insert_pos = bisect_left(values, target)

print('Список:', values)
print('Искомое число:', target)
print('Индекс найденного элемента:', position)

