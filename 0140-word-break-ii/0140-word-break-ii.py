class Solution:

    # #####
    # s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]

    #####
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def  backstrack(start, path):
            if start == len(s):
                result.append(' '.join(path))
                return

            for word in wordDict:
                if (start + len(word) <= len(s) and s[start:start + len(word)] == word):
                    path.append(word)
                    backstrack(start + len(word), path)
                    path.pop()

        result = []
        backstrack(0, [])
        return result

        