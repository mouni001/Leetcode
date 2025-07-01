from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 1) Build max-heap
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(nums, i, n)
        # 2) Extract max one by one, shrinking the heap
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self._sift_down(nums, 0, end)
        return nums

    def _sift_down(self, nums: List[int], start: int, size: int) -> None:
        """
        Restore the max-heap property in nums[start:size], assuming
        its subtrees are already heaps.
        """
        root = start
        while True:
            left = 2 * root + 1
            if left >= size:
                break
            # pick the larger child
            child = left
            right = left + 1
            if right < size and nums[right] > nums[left]:
                child = right
            # if root is less than that child, swap and continue
            if nums[root] < nums[child]:
                nums[root], nums[child] = nums[child], nums[root]
                root = child
            else:
                break