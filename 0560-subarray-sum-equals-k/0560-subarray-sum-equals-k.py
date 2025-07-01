class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #   nums = 1,1,1 k = 2
        count = 0
        consum_freq = {0:1}
        cumulative_sum = 0 

        for num in nums:
            cumulative_sum += num


            if(cumulative_sum - k) in consum_freq:
                count += consum_freq[cumulative_sum - k]


            consum_freq[cumulative_sum] = consum_freq.get(cumulative_sum, 0) + 1

        return count
