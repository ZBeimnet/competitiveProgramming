from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        in_edges = [0] * numCourses

        # build the adjacency list and count the incoming edges
        for i in range(len(prerequisites)):
            courses[prerequisites[i][1]].append(prerequisites[i][0])
            in_edges[prerequisites[i][0]] += 1

        # start traversing courses with no prerequisites
        queue = deque()
        top_sort = []
        for i in range(len(in_edges)):
            if not in_edges[i]:
                queue.append(i)

        while queue:
            current = queue.popleft()
            top_sort.append(current)

            for course in courses[current]:
                in_edges[course] -= 1
                if in_edges[course] == 0:
                    queue.append(course)

        return ([], top_sort)[numCourses == len(top_sort)]
