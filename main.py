def linear_search_all(values, target):
    positions = []
    comparisons = 0

    for index in range(len(values)):
        comparisons += 1
        if values[index] == target:
            positions.append(index)

    return positions, comparisons


values = [12, 12, 37, 54, 62, 38, 58, 5, 69]
target = 12

positions, comparisons = linear_search_all(values, target)

print('Список:', values)
print('Искомое число:', target)
print('Индексы вхождений:', positions)
print('Количество вхождений:', len(positions))
print('Количество сравнений:', comparisons)

