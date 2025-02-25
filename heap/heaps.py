def max_heapify(arr, i, n):
    left = 2 * i + 1  # 0-based index
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, n)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Start from the last non-leaf node
        max_heapify(arr, i, n)


def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr)
    print(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the root (max) with the last element
        max_heapify(arr, 0, i)  # Restore heap property on reduced heap

    return arr


arr = [3, 5, 2, 1, 4]
sorted_arr = heap_sort(arr[:])  # [:] to avoid modifying original array
print(sorted_arr)  # Output: [1, 2, 3, 4, 5]
