class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """   j = word2
        dp = [[1,2]i = word1
              [3, 4]]
        word1 = "horse" -> 6
        word2 = "ros" -> 4
        dp = [[0,1,2,3],
              [1,0,0,0],
              [2,0,0,0],
              [3,0,0,0],
              [4,0,0,0],
              [5,0,0,0]
            ]
        i = 1
        """
        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range (m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j


        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) 
        return dp[m][n]       