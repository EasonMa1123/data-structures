class node:
    def __init__(self,value):
        self.__value = value
        self.__next = None
    
    def setNextNode(self,node):
        self.__next = node

    def getValue(self):
        return self.__value
    
    def getNextNode(self):
        return self.__next




class LinkedList:
    
    def __init__(self):
        self.__headNode = None
        self.__lastNode = None

    def appendNode(self,value):
        new_node = node(value)
        if self.__headNode == None:
            self.__headNode = new_node
            self.__lastNode = new_node
        else:
            self.__lastNode.setNextNode(new_node)
            self.__lastNode = new_node


    def arrayLinkList(self):
        if self.__headNode == None:
            return -1
        current_node = self.__headNode
        linklist_array = []
        while current_node != None:
            linklist_array.append(current_node.getValue())
            current_node = current_node.getNextNode()

        return linklist_array
    
    def listlen(self):
        if self.__headNode == None:
            return 0
        current_node = self.__headNode
        list_length = 0
        while current_node != None:
            list_length+=1
            current_node = current_node.getNextNode()

        return list_length
        
    



