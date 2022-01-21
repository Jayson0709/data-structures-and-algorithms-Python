list1 = [15, 24, 2, 99, 74, 22, 11, 5, 109, 33, 50, 79, 128, 4]


def merge(left, right):
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(left) and index2 < len(right):
        if left[index1] <= right[index2]:
            result.append(left[index1])
            index1 += 1
        else:
            result.append(right[index2])
            index2 += 1
    result += left[index1:]
    result += right[index2:]
    
    return result


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid_point = len(arr) // 2
    left_part = arr[:mid_point]
    right_part = arr[mid_point:]
    left_part = mergesort(left_part)
    right_part = mergesort(right_part)
    return merge(left_part, right_part)


if __name__ == "__main__":
    list1 = mergesort(list1)
    print(list1)
