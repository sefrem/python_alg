
def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    less = [i for i in arr if i < pivot]
    greater = [i for i in arr if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([101, 14, 23, 17, 3,1, 5, 4, 7, 5, 21, 13, 65]))