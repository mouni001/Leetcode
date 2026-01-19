class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_num_idx = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in dict_num_idx:
                return [dict_num_idx[number], i]
            dict_num_idx[nums[i]] = i

