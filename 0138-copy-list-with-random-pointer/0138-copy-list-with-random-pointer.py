"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        #dictionary to map from the original to the copy
        node_map = {}


        current = head

        while current:
            node_map[current] = Node(current.val)
            current = current.next


        current = head

        while current:
            if current.next:
                node_map[current].next = node_map[current.next]

            if current.random:
                node_map[current].random =node_map[current.random]
            current = current.next

        return node_map[head]
            

