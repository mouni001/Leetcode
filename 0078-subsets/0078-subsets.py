class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []


        def backtracking(start, current_subset):
            result.append(current_subset[:])

            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtracking(i + 1, current_subset)
                current_subset.pop()

        backtracking(0,[])
        return result