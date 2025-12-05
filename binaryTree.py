class TreeNode:
    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None
    
    def left(self,node):
        self.__left = node
    
    def right(self,node):
        self.__right = node

    def check_left(self):
        return self.__left
    
    def check_right(self):
        return self.__right
    
    def getValue(self):
        return self.__value

class Tree:
    def __init__(self):
        self.__root = None
    
    def addNode(self,value):
        if self.__root == None:
            self.__root = TreeNode(value)
        else:
            self.placeNode(self.__root,value)

    def placeNode(self,top,value):
        if value<top.getValue():
            if top.check_left() == None:
                top.left(TreeNode(value))
                return
            else:
                self.placeNode(top.check_left(),value)
        elif value>top.getValue():
            if top.check_right() == None:
                top.right(TreeNode(value))
                return
            else:
                self.placeNode(top.check_right(),value)
    def PreOrderPrintTree(self,root=None,first = True):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            print(root.getValue())
            self.PreOrderPrintTree(root.check_left(),False)
            
            self.PreOrderPrintTree(root.check_right(),False)       
    def InOrderPrintTree(self,root=None,first = True):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            self.InOrderPrintTree(root.check_left(),False)
            print(root.getValue())
            self.InOrderPrintTree(root.check_right(),False)       
    def PostOrderPrintTree(self,root=None,first = True):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            self.PostOrderPrintTree(root.check_left(),False)
            
            self.PostOrderPrintTree(root.check_right(),False)       
            print(root.getValue())
