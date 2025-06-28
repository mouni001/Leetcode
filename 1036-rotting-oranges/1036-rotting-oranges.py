from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0


        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(0,1), (1, 0), (0,-1), (-1, 0)]

        while queue and fresh_count >0:
            minutes += 1
            for _ in range(len(queue)):
                row, col =  queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc


                    if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        queue.append((new_row, new_col))



        return minutes if fresh_count == 0 else -1
             
        