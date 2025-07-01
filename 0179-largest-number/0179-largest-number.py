from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for  num in nums]

        def compare(x, y):
            if x + y > y + x:
                return -1 
            elif x + y < y + x:
                return 1
            else:
                return 0

        str_nums.sort(key = cmp_to_key(compare))

        result = "".join(str_nums)

        return result if result[0] != "0" else "0"