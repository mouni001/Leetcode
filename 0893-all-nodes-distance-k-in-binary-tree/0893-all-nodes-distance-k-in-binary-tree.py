
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        parent = {}

        def build_parent(node, par=None):
            if node:
                parent[node] = par
                build_parent(node.left, node)
                build_parent(node.right, node)
        build_parent(root)


        #BFS from target node
        queue = deque([(target, 0)])
        visited = {target}
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
                continue

            if dist < k:
                for neighbor in [node.left, node.right, parent[node]]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return result

        