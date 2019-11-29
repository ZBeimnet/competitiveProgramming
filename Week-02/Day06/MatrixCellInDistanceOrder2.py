# a better implementation of the problem


def order_cells_by_distance(row, column, r0, c0):
    matrix = [[] for x in range(row * column)]
    sorted_matrix = []
    ordering_cell = [r0, c0]

    for i in range(row):
        for j in range(column):
            current_element = [i, j]
            current_distance = calculate_distance(current_element, ordering_cell)
            matrix[current_distance].append(current_element)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sorted_matrix.append(matrix[i][j])

    return sorted_matrix


def calculate_distance(array1, array2):
    return abs(array1[0] - array2[0]) + abs(array1[1] - array2[1])


print(order_cells_by_distance(1, 2, 0, 0))
print(order_cells_by_distance(2, 2, 0, 1))
