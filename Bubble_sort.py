"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
wrong order.

"""


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                
                
array = [5, 1, 4, 2, 6, 9]
print(array)
bubble_sort(array)
print(array)

for i in array:
    print(i, end="  ")
