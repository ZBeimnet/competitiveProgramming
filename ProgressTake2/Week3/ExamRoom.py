# Leetcode's solution
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:
        if not self.students:
            self.students.append(0)
            return 0

        distance, student = self.students[0], 0
        for i, s in enumerate(self.students):
            if i:
                prev = self.students[i - 1]
                d = (s - prev) // 2
                if d > distance:
                    distance, student = d, prev + d

        d = self.N - 1 - self.students[-1]
        if d > distance:
            student = self.N - 1

        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)