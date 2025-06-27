from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s) #{'}
        max_freq = max(char_count.values())
        if max_freq > (len(s) + 1)//2:
            return ""

        heap = []

        for char, freq in char_count.items():
            entry = (-freq, char)
            heapq.heappush(heap, entry)


        result = []
        prev_char = None
        prev_freq = 0

        while heap:

            freq1, char1 = heapq.heappop(heap)
            freq1 = -freq1
            result.append(char1)

            if prev_freq > 0:
                heapq.heappush(heap, (-prev_freq, prev_char))

            prev_char = char1
            prev_freq = freq1 - 1

        return ''.join(result)
            
        