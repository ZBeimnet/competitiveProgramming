def beautify_string(s):
    string_length = len(s)
    question_mark = '?'

    prev_char = s[0]
    # check if it can be replaced
    for i in range(1, string_length):
        if prev_char != question_mark and s[i] != question_mark:
            if prev_char == s[i]:
                return -1
        else:
            prev_char = s[i]

    # find number of question_marks
    counter = 0
    for i in range(string_length):
        if s[i] == question_mark:
            counter += 1

    while counter > 0:
        replace_char = ""
        index = 0
        for i in range(string_length):
            if s[i] == question_mark:
                if i == 0:
                    replace_char = replace_questions_mark(None, s[i+1])
                    index = i
                elif i == string_length - 1:
                    replace_char = replace_questions_mark(s[i-1], None)
                    index = i
                else:
                    replace_char = replace_questions_mark(s[i-1], s[i+1])
                    index = i
                break
        s = s[:index] + replace_char + s[index+1:]
        counter -= 1

    return s


def replace_questions_mark(prev=None, nxt=None):
    chars = ['a', 'b', 'c']

    # if question_mark at the beginning
    if not prev and nxt:
        for i in range(len(chars)):
            if chars[i] != nxt:
                return chars[i]

    # if question_mark at the middle
    elif prev and nxt:
        for i in range(len(chars)):
            if chars[i] != prev and chars[i] != nxt:
                return chars[i]

    # if question_mark at the end
    else:
        for i in range(len(chars)):
            if chars[i] != prev:
                return chars[i]


def main():
    num_of_tests = eval(input())
    for i in range(num_of_tests):
        test = input()
        print(beautify_string(test))


main()
