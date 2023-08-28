class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        # this is the dequeue operation
        # reverse the s1 into s2 
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        # pop off the top val of s2 and store in var
        front = self.s2.pop()
        # reverse the s2 back into the s1 
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        # return the dequeued var 
        return front

    def peek(self) -> int:
        # reverse the s1 into s2
        # peek the top val of s2 and return it 
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        front = self.s2[-1]
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return front

    def empty(self) -> bool:
        return True if len(self.s1) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()