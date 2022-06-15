def find_smallest_index(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def sort_select(list):
    newList = []
    while len(list):
        smallest_index = find_smallest_index(list)
        newList.append(list.pop(smallest_index))
    return newList


print(sort_select([5, 7, 12, 1, 24]))
