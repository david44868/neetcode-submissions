class MinStack:

    # Correct
    def __init__(self):
        self.array = []
        self.minArray = []

    def push(self, val: int) -> None:
        self.array.append(val) # Correct
        val = min(val, self.minArray[-1] if self.minArray else val)
        self.minArray.append(val)

    # Correct
    def pop(self) -> None:
        self.array.pop()
        self.minArray.pop()

    # Correct
    def top(self) -> int:
        return self.array[-1]

    # Correct
    def getMin(self) -> int:
        return self.minArray[-1]

