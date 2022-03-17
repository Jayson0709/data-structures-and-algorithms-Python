list1 = [14, 79, 5, 15, 25, 90, 111, 2000, 79, 128]


def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


if __name__ == "__main__":
    bubble_sort(list1)
