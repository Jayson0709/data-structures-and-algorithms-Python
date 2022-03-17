def counting_sort(arr):
    if len(arr) < 2:
        return arr
    max_num = max(arr)
    count = [0] * (max_num + 1)
    for num in arr:
        count[num] += 1
    new_array = []
    for i in range(len(count)):
        for _ in range(count[i]):
            new_array.append(i)
    return new_array

list1 = [1, 10, 4, 112, 59, 22, 56, 90, 40, 23, 22, 19, 34]
print(counting_sort(list1))
    