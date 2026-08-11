class MinStack:

    def __init__(self):
        self.arr = []
        self.m = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.m or val <= self.m[-1]:
            self.m.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.m[-1]:
            self.m.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.m[-1]