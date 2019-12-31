def check_hash(password, hashed):
    pass_length = len(password)
    hash_length = len(hashed)
    diff = hash_length - pass_length

    if diff < 0:
        return "NO"

    count = 0
    while diff >= 0:
        hash_slice = hashed[count: pass_length+count]
        if is_anagram(hash_slice, password):
            return "YES"
        count += 1
        diff -= 1

    return "NO"


def is_anagram(string1, string2):
    string1_count = [0] * 200
    string2_count = [0] * 200
    result = True

    for char in string1:
        string1_count[ord(char)] += 1

    for char in string2:
        string2_count[ord(char)] += 1

    if string1_count != string2_count:
        result = False

    return result


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        password = input()
        hashed = input()
        print(check_hash(password, hashed))


main()





