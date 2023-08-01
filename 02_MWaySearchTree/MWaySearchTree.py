MAX = 11
MIN = 1

class node:
    def __init__(self):
        self.count = -1
        self.value = [-1]*(MAX + 1)
        self.child = [None]*(MAX + 1)

class MWaySearchTree:
    def __init__(self, orden):
        self.root = None
        self.orden = 3
        if (orden < 3):
            print("Orden debe ser Mayor o igual a 3")
        else:
            self.orden = orden

    # Searches value in the node
    def search(val, root, pos):
        # if root is None then return
        if (root == None):
            return None
        else :
            # if node is found
            if (searchnode(val, root, pos)):
                return root
            # if not then search in child nodes
            else:
                return search(val, root.child[pos], pos)
    # Searches the node
    def searchnode(val, n, pos):
        # if val is less than node.value[1]
        if (val < n.value[1]):
            pos = 0
            return 0
        # if the val is greater
        else :
            pos = n.count
            # check in the child array
            # for correct position
            while ((val < n.value[pos]) and pos > 1):
                pos-=1
            if (val == n.value[pos]):
                return 1
            else:
                return 0
    # Inserts a value in the m-Way tree
    def insert(val, root):
        # Function setval() is called which
        # returns a value 0 if the new value
        # is inserted in the tree, otherwise
        # it returns a value 1
        i,c=0,None
        flag = setval(val, root, i, c)
    
        if (flag) :
            n = node()
            n.count = 1
            n.value[1] = i
            n.child[0] = root
            n.child[1] = c
            return n
        
        return root
    # Sets the value in the node
    def setval(val, n, p, c):
        k=0
    
        # if node is None
        if (n == None) :
            p = val
            c = None
            return 1
        
        else :
    
            # Checks whether the value to be
            # inserted is present or not
            if (searchnode(val, n, k)):
                print("Key value already exists")
    
            # The if-else condition checks whether
            # the number of nodes is greater or less
            # than the maximum number. If it is less
            # then it inserts the new value in the
            # same level node, otherwise, it splits the
            # node and then inserts the value
            if (setval(val, n.child[k], p, c)) :
    
                # if the count is less than the max
                if (n.count < MAX) :
                    fillnode(p, c, n, k)
                    return 0
                
                else :
    
                    # Insert by splitting
                    split(p, c, n, k, p, c)
                    return 1
            return 0
    # Adjusts the value of the node
    def fillnode(val, c, n, k):
        i=0
    
        # Shifting the node by one position
        for i in range(n.count, k, -1):
            n.value[i + 1] = n.value[i]
            n.child[i + 1] = n.child[i]
        
        n.value[k + 1] = val
        n.child[k + 1] = c
        n.count+=1
    # Splits the node
    def split(val, c, n, k, y, newnode):
        i, mid=0,0
        if (k <= MIN):
            mid = MIN
        else:
            mid = MIN + 1
    
        # Allocating the memory for a new node
        newnode = node()
    
        for i in range(mid + 1,MAX+1) :
            newnode.value[i - mid] = n.value[i]
            newnode.child[i - mid] = n.child[i]
        
    
        newnode.count = MAX - mid
        n.count = mid
    
        # it checks whether the new value
        # that is to be inserted is inserted
        # at a position less than or equal
        # to minimum values required in a node
        if (k <= MIN):
            fillnode(val, c, n, k)
        else:
            fillnode(val, c, newnode, k - mid)
    
        y = n.value[n.count]
        newnode.child[0] = n.child[n.count]
        n.count-=1
    # Deletes value from the node
    def delete(val, root):
        temp=None
        if (not delhelp(val, root)) :
            print()
            print("value not found.")
        
        else :
            if (root.count == 0) :
                temp = root
                root = root.child[0]      
        
        return root
    # Helper function for del()
    def delhelp(val, root):
        i,flag=None,None
        if (root == None):
            return 0
        else :
    
            # Again searches for the node
            flag = searchnode(val,root,i)
    
            # if flag is true
            if (flag) :
                if (root.child[i - 1]) :
                    copysucc(root, i)
                    # delhelp() is called recursively
                    flag = delhelp(root.value[i],
                                    root.child[i])
                    if (not flag):
                        print()
                        print("value not found.")
                    
                
                else:
                    clear(root, i)
            
            else :
                # Recursion
                flag = delhelp(val, root.child[i])
            
    
            if (root.child[i] != None) :
                if (root.child[i].count < MIN):
                    restore(root, i)
            
            return flag
    # Removes the value from the
    # node and adjusts the values
    def clear(m, k):
        for i in range(k + 1,m.count+1) :
            m.value[i - 1] = m.value[i]
            m.child[i - 1] = m.child[i]
        
        m.count-=1
    
    # Copies the successor of the
    # value that is to be deleted
    def copysucc(m, i):
        temp = p.child[i]
        while (temp.child[0]):
            temp = temp.child[0]
        p.value[i] = temp.value[i]

    # Adjusts the node
    def restore(m, i):
        if (i == 0):
            if (m.child[1].count > MIN):
                leftshift(m, 1)
            else:
                merge(m, 1)
        
        else :
            if (i == m.count) :
                if (m.child[i - 1].count > MIN):
                    rightshift(m, i)
                else:
                    merge(m, i)
            
            else :
                if (m.child[i - 1].count > MIN):
                    rightshift(m, i)
                else :
                    if (m.child[i + 1].count > MIN):
                        leftshift(m, i + 1)
                    else:
                        merge(m, i)
    # Adjusts the values and children
    # while shifting the value from
    # parent to right child
    def rightshift(m, k):
        temp = m.child[k]
    
        # Copying the nodes
        for i in range(temp.count,0,-1) :
            temp.value[i + 1] = temp.value[i]
            temp.child[i + 1] = temp.child[i]
        
        temp.child[1] = temp.child[0]
        temp.count+=1
        temp.value[1] = m.value[k]
    
        temp = m.child[k - 1]
        m.value[k] = temp.value[temp.count]
        m.child[k].child[0] = temp.child[temp.count]
        temp.count-=1
        
    # Adjusts the values and children
    # while shifting the value from
    # parent to left child
    def leftshift(m, k):
    
        temp = m.child[k - 1]
        temp.count+=1
        temp.value[temp.count] = m.value[k]
        temp.child[temp.count] = m.child[k].child[0]
    
        temp = m.child[k]
        m.value[k] = temp.value[1]
        temp.child[0] = temp.child[1]
        temp.count-=1
    
        for i in range(1, temp.count+1):
            temp.value[i] = temp.value[i + 1]
            temp.child[i] = temp.child[i + 1]
    
    # Merges two nodes
    def merge(m, k):
        temp1 = m.child[k]
        temp2 = m.child[k - 1]
        temp2.count+=1
        temp2.value[temp2.count] = m.value[k]
        temp2.child[temp2.count] = m.child[0]
    
        for i in range(temp1.count+1):
            temp2.count+=1
            temp2.value[temp2.count] = temp1.value[i]
            temp2.child[temp2.count] = temp1.child[i]
        
        for i in range(k,m.count):
            m.value[i] = m.value[i + 1]
            m.child[i] = m.child[i + 1]
        
        m.count-=1