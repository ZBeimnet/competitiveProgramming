def maximum_instruction(instruction):
    visited = []
    cur_pos = [0, 0]
    new_instruction = ""
    # traverse and store their position
    for i in instruction:
        if i == 'U':
            cur_pos[1] += 1
            current = [cur_pos[0], cur_pos[1]]
            visited.append(current)
        elif i == 'D':
            cur_pos[1] -= 1
            current = [cur_pos[0], cur_pos[1]]
            visited.append(current)
        elif i == 'R':
            cur_pos[0] += 1
            current = [cur_pos[0], cur_pos[1]]
            visited.append(current)
        else:
            cur_pos[0] -= 1
            current = [cur_pos[0], cur_pos[1]]
            visited.append(current)

    return visited


print(maximum_instruction("RULLLRRRUUUDDD"))
