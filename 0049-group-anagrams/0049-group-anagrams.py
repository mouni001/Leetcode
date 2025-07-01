class Solution:

    '''
    strs = ["eat', "ate","tan", "tea", "nat", "bat"]
    '''
   
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))

            if sorted_str not in anagram_groups:
                anagram_groups[sorted_str] = []

            anagram_groups[sorted_str].append(s)

        return list(anagram_groups.values())


