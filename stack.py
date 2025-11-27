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
    
    def printStack(self):
        return self.arr
    
    def sort(self):
        if self.pop == -1:
            return 
        temp_item = self.pop()
        tempStack1 = Stack(self.capacity)
        tempStack2 = Stack(self.capacity)
        compare_Item = self.pop()
        while not(self.isSorted):
            self.split(temp_item,compare_Item,tempStack1,tempStack2)
            self.merge(temp_item,tempStack1,tempStack2)
        
  
        
    def isSortedhelper(self,n):
        arr = self.arr
        # Base case
        if (n == 0 or n == 1):
            return True
            
        # Check if current and previous elements are in order
        # and recursively check the rest of the array
        return (arr[n - 1] >= arr[n - 2] and self.isSortedhelper(arr, n - 1))
                
    def isSorted(self):
        
        n = len(self.arr)
        
        return self.isSortedhelper( n)

    def split(self,temp_item,compare_Item,stack1,stack2):
        while True:
            if temp_item >= compare_Item:
                stack1.push(compare_Item)
            elif temp_item < compare_Item:
                stack2.push(compare_Item)
            compare_Item = self.pop()
            if compare_Item == -1:
                return

    def merge(self,temp_item,stack1,stack2):
        while stack1.isEmpty() == False:
            self.push(stack1.pop())
        self.push(temp_item)
        while stack2.isEmpty() == False:
            self.push(stack2.pop())
