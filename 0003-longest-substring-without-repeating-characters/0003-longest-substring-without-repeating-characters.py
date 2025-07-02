class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        s = "abcabcbb"
        return max_length = 3

        right = 0 s[0] = a, char_set = {'a'}
        '''


        if not s:
            return 0

        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length  = max(max_length , right - left + 1)

        return max_length 