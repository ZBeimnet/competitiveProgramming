"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if not employees:
            return 0

        employee_importance = {}
        employee_subordinates = {}

        # creating a hash-map of the form id: importance and id: [sub...]
        for employee in employees:
            employee_importance[employee.id] = employee.importance
            employee_subordinates[employee.id] = employee.subordinates

        # finding the total importance using bfs
        total = 0
        stack = [id]
        while stack:
            current_vertex = stack.pop()
            total += employee_importance[current_vertex]

            for sub_id in employee_subordinates[current_vertex]:
                stack.append(sub_id)

        return total