class SORTracker:

    def __init__(self):
        self.location = []
        self.query_count = 0
        

    def add(self, name: str, score: int) -> None:
        location = (-score, name)

        left, right = 0, len(self.location)
        while left < right:
            mid = (left + right) //2

            if self.location[mid] <= location:
                left = mid + 1
            else:
                right = mid

        self.location.insert(left, location)

    def get(self) -> str:
        result = self.location[self.query_count][1]
        self.query_count += 1
        return result

# tracker = SORTracker()
# tracker.add("bradford", 2)
# tracker.add("bradford", 3)
# print(tracker.get())
# tracker.add("alps", 2)
# print(tracker.get())
# tracker.add("orland", 2)
# print(tracker.get())


        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()