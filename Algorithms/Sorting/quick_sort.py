def partition(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        if low < high:
            arr[low] = arr[high]
        while low < high and arr[low] < key:
            low += 1
        if low < high:
            arr[high] = arr[low]
    arr[low] = key
    return low


def quicksort(arr, low, high):
    if low < high:
        key_index = partition(arr, low, high)
        quicksort(arr, low, key_index)
        quicksort(arr, key_index + 1, high)


if __name__ == "__main__":
    list1 = [15, 24, 2, 99, 74, 22, 11, 5, 109, 33, 50, 79, 128, 4]
    low = 0
    high = len(list1) - 1
    quicksort(list1, low, high)
    print(list1)
