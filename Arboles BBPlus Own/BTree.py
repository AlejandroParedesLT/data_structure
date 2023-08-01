class BTree:
    class BTreeNode:
        def __init__(self, leaf=False):
            self.leaf = leaf
            self.keys = []
            self.child = []

    def __init__(self, t):
        self.root = self.BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = self.BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.keys.insert(i + 1, k)
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child) > i and len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)



    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = self.BTreeNode(y.leaf)
        x.keys.insert(i, y.keys[t - 1])
        x.child.insert(i + 1, z)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.child = y.child[t:]
            y.child = y.child[:t]


    def inorder_traversal(self, x):
        if x is not None:
            i = 0
            while i < len(x.keys):
                self.inorder_traversal(x.child[i])
                print(x.keys[i])
                i += 1
            self.inorder_traversal(x.child[len(x.keys)])  # Traverse the rightmost child

