class Node:
    __slots__ = ("key","value","prev","next")
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}               # key -> Node

        # Dummy head/tail so we never have to check for None
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        # Always insert right after head
        node.next       = self.head.next
        node.prev       = self.head
        self.head.next.prev = node
        self.head.next  = node

    def _remove_node(self, node: Node):
        # Unlink from list
        prev = node.prev
        nxt  = node.next
        prev.next = nxt
        nxt.prev  = prev

    def _move_to_front(self, node: Node):
        # Bump this node as most-recently-used
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        # mark as recently used
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            # update existing
            node.value = value
            self._move_to_front(node)
        else:
            # insert brand-new
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)

            # if over capacity, evict LRU
            if len(self.cache) > self.capacity:
                # tail.prev is the LRU node
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]
