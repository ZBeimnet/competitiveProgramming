def is_anagram(string1, string2):
    string1_count = [0] * 26
    string2_count = [0] * 26
    result = True

    for char in string1:
        string1_count[ord(char)-97] += 1

    for char in string2:
        string2_count[ord(char)-97] += 1

    if string1_count != string2_count:
        result = False

    return result


print(is_anagram("anagram", "nagaram"))



