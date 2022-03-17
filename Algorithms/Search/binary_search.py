def binary_search(arr, k):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if k < arr[mid]:
            right = mid - 1
        if k > arr[mid]:
            left = mid + 1
        else:
            return mid
    return -1

arr = [1, 4, 5, 7, 19, 22, 34, 45, 50, 55, 60, 65, 70, 99]
k = 50

print(binary_search(arr, k))
