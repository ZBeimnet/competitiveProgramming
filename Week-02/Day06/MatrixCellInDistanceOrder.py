def order_cells_by_distance(row, column, r0, c0):
    matrix = [[i, j] for i in range(row) for j in range(column)]
    sorted_matrix = []
    ordering_cell = [r0, c0]

    max_distance = calculate_maximum_distance(matrix, ordering_cell)
    min_distance = 0
    while min_distance <= max_distance:
        for i in range(len(matrix)):
            if calculate_distance(matrix[i], ordering_cell) == min_distance:
                sorted_matrix.append(matrix[i])
        min_distance += 1

    return sorted_matrix


def calculate_maximum_distance(matrix, ordering_cell):
    max_distance = 0

    for i in range(len(matrix)):
        current_distance = calculate_distance(matrix[i], ordering_cell)
        if current_distance > max_distance:
            max_distance = current_distance

    return max_distance


def calculate_distance(array1, array2):
    return abs(array1[0] - array2[0]) + abs(array1[1] - array2[1])


print(order_cells_by_distance(1, 2, 0, 0))
print(order_cells_by_distance(2, 2, 0, 1))
