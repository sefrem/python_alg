max_weight = 5

items_names = ["water",
               "book",
               "food",
               "jacket",
               "camera",
               ]

items = {
    "weight": [1, 1, 2, 4, 1],
    "value": [7, 6, 9, 9, 8]
}


def calculate():
    table = [[0 for x in range(max_weight)] for y in range(len(items_names))]
    for i in range(0, len(table)):
        items_weight = items['weight'][i]
        items_value = items['value'][i]
        for j in range(0, len(table[0])):
            if i == 0:
                table[i][j] = items_value if items_weight <= j + 1 else 0
            elif j == 0:
                table[i][j] = max(table[i - 1][j], items_value if items_weight <= j + 1 else 0)
            else:
                table[i][j] = max(table[i - 1][j], items_value + table[i - 1][j - items_weight]
                if items_weight + items['weight'][j - items_weight] <= j + 1
                else items_value if items_weight <= j + 1 else 0)

    return table


print(calculate())
