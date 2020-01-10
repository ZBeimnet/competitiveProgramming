class Solution:
    def fractionAddition(self, expression: str) -> str:
        # extracting out each fraction from expression
        fractions_stack = []
        start_pt = 0
        for i in range(1, len(expression)):
            if expression[i] == '/':
                end_pt = i + 1
                while end_pt <= len(expression) - 1:
                    if expression[end_pt] in "+-":
                        break
                    end_pt += 1
                current_fraction = expression[start_pt:end_pt]
                fractions_stack.append(current_fraction)
                start_pt = end_pt

        # popping two fractions --> adding them --> and pushing their sum back
        while len(fractions_stack) > 1:
            f1 = fractions_stack.pop()
            f2 = fractions_stack.pop()
            fractions_stack.append(self.add_two_fractions(f1, f2))

        return fractions_stack.pop()

    def add_two_fractions(self, f1, f2):
        # extracting out each number from the fractions
        f1 = f1.split("/")
        numerator1 = int(f1[0])
        denominator1 = int(f1[1])
        f2 = f2.split("/")
        numerator2 = int(f2[0])
        denominator2 = int(f2[1])

        # summing them up
        new_numerator = (numerator1 * denominator2) + (denominator1 * numerator2)
        new_denominator = denominator1 * denominator2

        current_gcd = self.gcd(abs(new_numerator), abs(new_denominator))

        return str(new_numerator // current_gcd) + "/" + str(new_denominator // current_gcd)

    def gcd(self, num1, num2):
        if num1 == 0:
            return num2
        return self.gcd(num2 % num1, num1)


