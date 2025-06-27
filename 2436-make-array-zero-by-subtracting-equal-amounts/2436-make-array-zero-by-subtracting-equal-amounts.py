class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # positive_nums = set(num for num in nums if num > 0)

        positive_nums = set()

        for num in nums:
            if num > 0:
                positive_nums.add(num)

        return len(positive_nums)
        