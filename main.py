# Сортировка кучей.

def heap_build(array_in, heap_size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and array_in[index] < array_in[left]:
        largest = left

    if right < heap_size and array_in[largest] < array_in[right]:
        largest = right

    if largest != index:
        array_in[index], array_in[largest] = array_in[largest], array_in[index]

        heap_build(array_in, heap_size, largest)


def heap_sort(arr):
    num = len(arr)

    for i in range(num, -1, -1):
        heap_build(arr, num, i)

    for i in range(num - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap_build(arr, i, 0)


array = [15, 8, 9, 12, 18, 7, 3, 10]
print(array)
heap_sort(array)
print("Sorted array ", array)
