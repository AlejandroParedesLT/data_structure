from BinarySearchTree import BinarySearchTree

def main():
    s = input("Enter a list of numbers: ")
    lst = s.split(sep=",")
    #lst = list(s)
    tree = BinarySearchTree()
    
    for x in lst:
        '''pdb.set_trace() '''
        tree.insert(float(x))
        
    #for x in tree:
        #print(x)
    
    tree.print_tree()

if __name__ == "__main__":
    main()