import pdb
  
class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class. 
    class Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
       
        def getVal(self):
            #pdb.set_trace()
            return self.val
        
        def setVal(self,newval):
            self.val = newval
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self,newleft):
            self.left = newleft
            
        def setRight(self,newright):
            self.right = newright
            
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
                    
            yield self.val
            
            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
    def __init__(self, root=None):
        self.root = root
        
    def insert(self,val):
        self.root = self.__insert(self.root,val)
        
    def __insert(self,root,val):
        if root == None:
            return self.Node(root,val)
        pdb.set_trace()
        if val < self.root.getVal():
            root.setLeft(self.__insert(root.getLeft(),val))
        else:
            root.setRight(self.__insert(root.getRight(),val))
            
        return root
        
    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"
 
def main():
    s = input("Enter a list of numbers: ")
    lst = s.split(sep=",")
    #lst = list(s)
    tree = BinarySearchTree()
    
    for x in lst:
        '''pdb.set_trace() '''
        tree.insert(float(x))
        
    for x in tree:
        print(x)
    
    tree.__str__()

if __name__ == "__main__":
    main()