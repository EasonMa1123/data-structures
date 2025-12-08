class node:
    def __init__(self,value):
        self.__value = value

    def getValue(self):
        return self.__value

class edge:
    def __init__(self):
        self.__nodeHead = None
        self.__nodeTail = None
        self.__weight = 0
    
    def connect(self,node1,node2,weight):
        self.__nodeHead = node1
        self.__nodeTail = node2

    def setWeight(self,weight):

        self.__weight = weight

class graph:
    def __init__(self):
        pass

    def addNode(self,value):
        new_node = node(value)
