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
        if top.getValue()>value:
            if top.check_left() == None:
                top.left(TreeNode(value))
                return
            else:
                self.placeNode(top.check_left(),value)
        elif top.getValue()<value:
            if top.check_right() == None:
                top.right(TreeNode(value))
                return
            else:
                self.placeNode(top.check_right(),value)
    def printTree(self,root=None):
        
        if root == None:
            root = self.__root
        print(root.getValue())
        if root :
            self.printTree(root.check_left())
            print(root.getValue())
            self.printTree(root.check_right())
        else:
            return
