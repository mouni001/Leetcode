class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        pos = neg = 0
        max_len = 0

        for num in nums:
            if num == 0:
                pos = neg = 0

            elif num > 0:
                pos = pos + 1 
                neg = neg +1 if neg > 0 else 0

            else:
                new_pos = neg + 1 if neg > 0 else 0 
                new_neg = pos + 1
                pos = new_pos
                neg = new_neg
            max_len = max(max_len, pos)

        return max_len
        