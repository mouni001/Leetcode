class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data.append(key)
        

    def remove(self, key: int) -> None:
        for i, val in enumerate(self.data):
            if val == key:
                self.data.pop(i)
                return

        

    def contains(self, key: int) -> bool:
        for val in self.data:
            if val == key:
                return True
        return False

    def __len__(self):
        return len(self.data)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)