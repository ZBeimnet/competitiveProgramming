class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.dfs([], n, n, result)
        return result

    def dfs(self, current, op_count, cl_count, result):
        if op_count == 0 and cl_count == 0:
            return result.append("".join(current))
        elif op_count == 0:
            return result.append("".join(current + [")" * cl_count]))

        if op_count:
            self.dfs(current + ["("], op_count - 1, cl_count, result)
        if cl_count > op_count:
            self.dfs(current + [")"], op_count, cl_count - 1, result)