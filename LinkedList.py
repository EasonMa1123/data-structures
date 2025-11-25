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
        self.__listLength = 0

    def appendNode(self,value):
        new_node = node(value)
        if self.__headNode == None:
            self.__headNode = new_node
            self.__lastNode = new_node
        else:
            self.__lastNode.setNextNode(new_node)
            self.__lastNode = new_node
        self.__listLength +=1


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
        return self.__listLength
    
    def insertNode(self,value,index:int):
        if index > self.__listLength:
            return -1
        
        if self.__headNode == None:
            return -1
        
        new_node = node(value)
        current_node = self.__headNode
        current_node_index = 0
        
        while current_node_index < index:
            current_node = current_node.getNextNode()
            current_node_index+=1
        
        
        pointer_node = current_node.getNextNode()
        current_node.setNextNode(new_node)
        new_node.setNextNode(pointer_node)
        
        self.__listLength +=1
    
    def findNodeValue(self,index:int):
        if index > self.__listLength:
            return -1
        
        if self.__headNode == None:
            return -1
        
        current_node = self.__headNode
        current_node_index = 0
        
        while current_node_index < index:
            
            current_node = current_node.getNextNode()
            current_node_index+=1
        return current_node.getValue()
    
    def findNodeIndex(self,value):
        if self.__headNode == None:
            return -1
        current_node = self.__headNode
        current_node_value = current_node.getValue()
        current_node_index = 0
        while current_node != None :
            if  current_node_index >= self.__listLength-1:
                return -1
            if current_node_value == value:
                break
            current_node = current_node.getNextNode()
            current_node_value = current_node.getValue()
            current_node_index +=1
            
            

        return current_node_index


    def remove(self,value):
        if self.__headNode == None:
            return -1
        
        current_node = self.__headNode
        current_node_value = current_node.getValue()
        node_counter = 0
        previous_node = None
        while current_node_value != value:
            node_counter += 1 
            if node_counter > self.__listLength:
                return -1
            previous_node = current_node
            current_node = current_node.getNextNode()
            current_node_value = current_node.getValue()
        if previous_node == None:
            self.__headNode = current_node.getNextNode()
        else:
            previous_node.setNextNode(current_node.getNextNode())
        
        
    '''
    def sort(self):
      if self.__headNode == None:
            return 
      
      item_1 = self.__headNode
      item_2 = item_1.getNextNode()
      
      while item_2.getNextNode() != None:
        temp = None
        
        if item_2.getValue()>item_1.getValue():
          temp = item_1
          item_1.setNextNode(item_2.getNextNode())
          if item_1 == self.__headNode:
            self.__headNode = item_2
          item_1 = item_2
          item_2.setNextNode(item_1)
          item_2 = temp
        item_1 = item_2
        item_2 = item_2.getNextNode()
      
'''
    
