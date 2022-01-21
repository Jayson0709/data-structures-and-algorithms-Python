# 两个有序数组找第K大

def partition(arr, left, right):
    v = arr[left]
    j = left
    i = left + 1
    while i <= right:
        if arr[i] >= v:
            arr[j + 1], arr[i] = arr[i], arr[j + 1]
            j += 1
        i += 1
    arr[left], arr[j] = arr[j], arr[left]
    return j


def quick_sort(arr, left, right, k):
    if left >= right:
        return left
    pivot = partition(arr, left, right)
    if pivot + 1 == k:
        return pivot
    elif pivot + 1 > k:
        return quick_sort(arr, left, pivot - 1, k)
    else:
        return quick_sort(arr, pivot + 1, right, k)


def find_kth_largest(arr1, arr2, k):
    arr = arr1 + arr2
    n = len(arr)
    if (k > n):
        return
    index = quick_sort(arr, 0, n - 1, k)
    return arr[index]


list1 = [1, 3, 5, 7, 10, 15, 29]
list2 = [4, 8, 9, 14, 16, 27, 30]
k = 3

print(find_kth_largest(list1, list2, k))
result = list1 + list2
result.sort()
print(result)
