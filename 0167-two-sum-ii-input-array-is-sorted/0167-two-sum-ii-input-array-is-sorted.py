class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        numbers = [2,7,11,15], target = 9
        left = 0, right = 3, current_sum = 17 > 9 
        left = 0, right = 2, current_sum = 13 > 9
        left = 0, right = 1, current_sum = 9 == 9


        '''
        left =0 
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right+ 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []