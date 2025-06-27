class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        positive_nums = set(num for num in nums if num > 0)

        return len(positive_nums)
        