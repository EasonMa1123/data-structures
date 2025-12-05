class TreeNode:
    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None
    
    def left(self,node):
        self.__left = node
    
    def right(self,node):
        self.__right = node

    def getLeft(self):
        return self.__left
    
    def getRight(self):
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
            if top.getLeft() == None:
                top.left(TreeNode(value))
                return
            else:
                self.placeNode(top.getLeft(),value)
        elif value>top.getValue():
            if top.getRight() == None:
                top.right(TreeNode(value))
                return
            else:
                self.placeNode(top.getRight(),value)
    def PreOrderPrintTree(self,root=None,first = True,array=[]):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            array.append(root.getValue())
            
            self.PreOrderPrintTree(root.getLeft(),False,array)
            
            self.PreOrderPrintTree(root.getRight(),False,array)    
        return array
    def InOrderPrintTree(self,root=None,first = True,array=[]):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            self.InOrderPrintTree(root.getLeft(),False,array)
            array.append(root.getValue())
            
            self.InOrderPrintTree(root.getRight(),False,array)  
        return array
    def PostOrderPrintTree(self,root=None,first = True,array=[]):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            self.PostOrderPrintTree(root.getLeft(),False,array)
            
            self.PostOrderPrintTree(root.getRight(),False,array)     
            array.append(root.getValue())  
              
        return array
    def getLevel(self,target,root="head",level=0):
        if root == "head":
            root = self.__root

        if root is None:
            return -1


        if root.getValue() == target:
            return level


        leftLevel = self.getLevel(target,root.getLeft(),  level + 1)
        if leftLevel != -1:
            return leftLevel

        return self.getLevel(target,root.getRight(),  level + 1)

    def printTree(self,node="None",level = 0):
        
        if node == "None":
            node = self.__root
        
        if node != None:
            self.printTree(node.getLeft(), level + 1)
            
            print(' ' * 4 * level + '-> ' + str(node.getValue()))
            self.printTree(node.getRight(), level + 1)
    
    def depth(self,root = "None"):
        if root == "None":
            root = self.__root
        if root is None:
            return -1

        ldepth = self.depth(root.getLeft())
        rdepth = self.depth(root.getRight())

        return max(ldepth, rdepth) + 1
