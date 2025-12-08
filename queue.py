class queue:
    def __init__(self,size):
        self.__arr = [None]*size
        self.__size = size
        self.__headPointerPosition = 0
        self.__endPointerPosition = 0


    def append(self,value):
        
        if self.__endPointerPosition<self.__size:
            self.__arr[self.__endPointerPosition] = value
            self.__endPointerPosition +=1
            if self.__endPointerPosition > self.__size:
                self.__endPointerPosition = 0
        else:
            return -1
        
    def dequeue(self):
        if len(self.__arr) == 0:
            return -1
        else:
            item = self.__arr[self.__headPointerPosition]
            self.__arr[self.__headPointerPosition] = None
            for i in range(self.__size):
                if i+1 < self.__size:
                    self.__arr[i] = self.__arr[i+1]
                    
                elif i+1 == self.__size:
                    self.__arr[i] = None
                    self.__endPointerPosition -=1
            return item
        
    def printQueue(self):
        return self.__arr
