class MinStack:

    def __init__(self):
        self.data = []
        self.mind = []
        
    def push(self, val: int) -> None:
        self.data.append(val)
        val = min(val, self.mind[-1] if self.mind else val)
        self.mind.append(val)
        
    def pop(self) -> None:
        self.data.pop()
        self.mind.pop()
        
    def top(self) -> int:
        return self.data[-1]
        
    def getMin(self) -> int:
        return self.mind[-1]
        
