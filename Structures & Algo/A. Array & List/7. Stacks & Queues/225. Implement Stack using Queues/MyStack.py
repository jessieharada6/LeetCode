class MyStack:

    def __init__(self):
        self.s1 = []

    def push(self, x: int) -> None:
        self.s1.append(x)  

    def pop(self) -> int:
        return self.s1.pop()
        # return self.s1.pop(-1)

    def top(self) -> int:
        return self.s1[-1]
    
    def empty(self) -> bool:
        return len(self.s1) == 0

# for langs that have queue
# use var top_element to record the top element
# for pop(), keep the last 2 elements, record the the second last as top element
# then delete the last element

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()