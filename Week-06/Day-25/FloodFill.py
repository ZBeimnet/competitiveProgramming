class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        new_image = image
        starting_pixel = new_image[sr][sc]

        if starting_pixel == newColor:
            return new_image

        col = len(new_image[0])
        row = len(new_image)

        stack = [[sr, sc]]

        while stack:
            current_vertex = stack.pop()

            new_image[current_vertex[0]][current_vertex[1]] = newColor

            # find valid neighbours
            neighbours = []
            connections = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for x, y in connections:
                if (0 <= current_vertex[0] + x < row) \
                        and (0 <= current_vertex[1] + y < col):
                    neighbours.append([current_vertex[0] + x, current_vertex[1] + y])

            for i in range(len(neighbours)):
                if starting_pixel == new_image[neighbours[i][0]][neighbours[i][1]]:
                    stack.append([neighbours[i][0], neighbours[i][1]])

        return new_image






