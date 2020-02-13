class Solution:
    def longestWord(self, words: List[str]) -> str:
        words_set = set()
        words_length = {}

        # putting every element in words_set for later checking
        for word in words:
            words_set.add(word)

        for i in range(len(words)):
            found = set()

            for j in range(len(words[i])):
                curr = words[i][:j + 1]
                if curr in words_set:
                    found.add(True)
                else:
                    found.add(False)
                    break

            if len(found) == 1 and True in found:
                length = len(words[i])
                if length in words_length:
                    words_length[length].append(words[i])
                else:
                    words_length[length] = [words[i]]

        max_length = -1
        for key in words_length.keys():
            if key > max_length:
                max_length = key

        if max_length != -1:
            result = words_length[max_length][0]
            for i in range(1, len(words_length[max_length])):
                if words_length[max_length][i] < result:
                    result = words_length[max_length][i]
            return result
        else:
            return ""