def binary_search(low, high, list, item):
    mid = (low + high) // 2
    guess = list[mid]

    if low > high:
        return None
    if guess == item:
        return mid
    return binary_search(mid + 1, high, list, item) if guess < item else binary_search(low, mid - 1, list, item)


list = [1, 3, 5, 7, 12, 22, 32, 43, 56, 99]

print(binary_search(0, len(list), list, 99))
