from BTree import BTree
from BPlusTree import BPlusTree

# Example usage of B-Tree
def example_b_tree():
    b_tree = BTree(3)  # Create a B-Tree with degree 3
    b_tree.insert(10)
    b_tree.insert(20)
    b_tree.insert(5)
    b_tree.insert(15)
    b_tree.insert(30)
    b_tree.insert(25)
    b_tree.insert(35)
    
    print("Inorder traversal of B-Tree:")
    b_tree.inorder_traversal(b_tree.root)

# Example usage of B+ Tree
def example_b_plus_tree():
    b_plus_tree = BPlusTree(3)  # Create a B+ Tree with degree 3
    b_plus_tree.insert(10, "Value 1")
    b_plus_tree.insert(20, "Value 2")
    b_plus_tree.insert(5, "Value 3")
    b_plus_tree.insert(15, "Value 4")
    b_plus_tree.insert(30, "Value 5")
    b_plus_tree.insert(25, "Value 6")
    b_plus_tree.insert(35, "Value 7")

    print("Inorder traversal of B+ Tree:")
    b_plus_tree.inorder_traversal(b_plus_tree.root)

# Run examples
if __name__ == '__main__':
    example_b_tree()
    print()
    example_b_plus_tree()
