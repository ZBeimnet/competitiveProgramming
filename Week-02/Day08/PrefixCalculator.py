def prefix_calculator(string_input):
    operators = ['+', '-', '*', '/']
    input_list = string_input.split()
    list_length = len(input_list)

    stack = []

    for i in range(list_length-1, -1, -1):
        if input_list[i] not in operators:
            stack.append(input_list[i])
        else:
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            if input_list[i] == '*':
                stack.append(operand1 * operand2)
            elif input_list[i] == '/':
                stack.append(operand1 / operand2)
            elif input_list[i] == '+':
                stack.append(operand1 + operand2)
            else:
                stack.append(operand1 - operand2)

    return stack.pop()


print(prefix_calculator("+ 4 * 3 12"))
print(prefix_calculator("+ * 4 3 12"))
print(prefix_calculator("- + * 4 5 3 10"))


