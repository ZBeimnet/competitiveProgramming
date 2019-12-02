def k_closest(points, k):
    points_length = len(points)

    if k == points_length:
        return points

    for i in range(points_length):
        index_of_minimum = i

        for j in range(i+1, points_length):
            if square(points[index_of_minimum]) > square(points[j]):
                index_of_minimum = j

        points[i], points[index_of_minimum] = points[index_of_minimum], points[i]

        if i == k:
            break

    return points[:k]


def square(point):
    return (point[0]*point[0]) + (point[1]*point[1])


print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
print(k_closest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]],
5))