class Solution:
    from collections import Counter
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = Counter(nums)

        for key, value in x.items():
            if value > 1:
                return True
        return False
        