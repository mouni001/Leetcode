class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer1 = 0
        pointer2 = 0
        count = 0

        while pointer2 < len(nums):
            if nums[pointer2] != val:
                nums[pointer1] = nums[pointer2]
                pointer1 += 1  
            pointer2 += 1
        return pointer1