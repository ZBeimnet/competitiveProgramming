def common_chars(strings):
    strings_count = {}
    for i in range(len(strings)):
        strings_count[strings[i]] = count_chars(strings[i])

    first_string_count = strings_count[strings[0]]
    common = [0] * 26
    if len(strings) > 1:
        for i in range(len(first_string_count)):
            if first_string_count[i] > 0:
                minimum = first_string_count[i]
                exists_in_all = True
                for j in range(1, len(strings)):
                    current_string = strings_count[strings[j]]
                    if current_string[i] > 0:
                        if current_string[i] < minimum:
                            minimum = current_string[i]
                    else:
                        exists_in_all = False
                        break

                if exists_in_all:
                    common[i] = minimum
    else:
        common = first_string_count
    result = []
    for i in range(len(common)):
        if common[i] > 0:
            for j in range(common[i]):
                result.append(chr(i+97))

    return result


def count_chars(string):
    count = [0] * 26
    for char in string:
        count[ord(char) - 97] += 1

    return count


print(common_chars(["cool","lock","cook"]))

