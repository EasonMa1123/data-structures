class Stack:
    # constructor
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0] * self.capacity
        self.top = -1

    # push operation
    def push(self, x):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = x

    # pop operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        val = self.arr[self.top]
        self.top -= 1
        return val

    # peek (or top) operation
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return -1
        return self.arr[self.top]

    # check if stack is empty
    def isEmpty(self):
        return self.top == -1

    # check if stack is full
    def isFull(self):
        return self.top == self.capacity - 1


