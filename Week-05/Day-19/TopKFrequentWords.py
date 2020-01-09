# a word class with custom comparator
import heapq
from typing import List


class Word:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __gt__(self, other):
        if self.count > other.count:
            return True
        elif self.count == other.count:
            return self.word < other.word
        else:
            return False


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        length = len(words)
        word_count = {}
        for i in range(length):
            if words[i] in word_count:
                word_count[words[i]] += 1
            else:
                word_count[words[i]] = 1

        max_heap = []
        for i in word_count:
            max_heap.append(Word(i, word_count[i]))

        heapq._heapify_max(max_heap)

        result_list = []
        for i in range(k):
            current = heapq._heappop_max(max_heap)
            result_list.append(current.word)

        return result_list