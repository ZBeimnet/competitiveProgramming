def reorganize_string(string):
    string_length = len(string)
    letter_count = [0] * 128
    organized_string = ""

    # counting the repetition of each letter
    for i in range(string_length):
        letter_count[ord(string[i])] += 1

    # ascii code for lower-case a & z
    a, z = 97, 122

    previous_letter = ""
    counter = string_length
    while counter > 0:
        max_index = 0
        for i in range(a, z+1):
            if letter_count[i] > letter_count[max_index] \
                    and chr(i) != previous_letter:
                max_index = i
        if max_index == 0:
            return ""
        else:
            organized_string += chr(max_index)
            previous_letter = chr(max_index)
            letter_count[max_index] -= 1
            counter -= 1

    return organized_string


print(reorganize_string("aaabc"))
