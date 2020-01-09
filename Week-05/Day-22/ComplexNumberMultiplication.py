class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = a.split("+")
        w = int(a[0])
        x = int(a[1][:-1])

        b = b.split("+")
        y = int(b[0])
        z = int(b[1][:-1])

        int_part = w * y - x * z
        complex_part = w * z + y * x

        return str(int_part) + "+" + str(complex_part) + "i"
