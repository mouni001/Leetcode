class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        island = 0


        def dfs (r, c):
            if(r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or visited[r][c]):
                return

            visited[r][c] = True

            dfs(r - 1, c) #up
            dfs(r + 1, c) #down
            dfs(r, c- 1) # left
            dfs(r, c+ 1) # right


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    island += 1

        return island


                