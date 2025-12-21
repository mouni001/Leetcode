class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # calculate the maximum frequency
        freq = {}
        for number in nums:
            freq[number] = freq.get(number, 0) + 1
        
        maximum_value = max(freq.values())
        count = 0
        for v in freq.values():
            if (v == maximum_value):
                count += v
        return count

