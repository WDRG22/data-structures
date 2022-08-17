# NODE-BASED BINARY TREE
# 
# Properties of a node-based binary tree:
# - The left subtree of a node contains only nodes with lesser than the node's key
# - The right subtree of a node contains only nodes with greater than the node's key
# - The left and right subtree must each also be a binary tree
# 
# Applications of trees:
# - Manipulate hierarchical data.
# - Make information easy to search (see tree traversal).
# - Manipulate sorted lists of data.
# - As a workflow for compositing digital images for visual effects.
# - Router algorithms
# - Form of a multi-stage decision-making (see business chess).
# 
# Types of binary trees:
# - Full binary tree: A Binary Tree is full if every node has 0 or 2 children. Following are examples of full binary tree.
# - Complete binary tree: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
# - Perfect Binary Tree: A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.
# - Balanced Binary Tree: A binary tree is balanced if height of the tree is O(Log n) where n is number of nodes. 
#    For Example, AVL tree maintain O(Log n) height by making sure that the difference between heights of left and right subtrees is 1.
#    Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there 
#    are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
# - A degenerate (or pathological) tree: A Tree where every internal node has one child. Such trees are performance-wise same as linked list.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    def preorder(self):
    # Print tree in preorder traversal (root, left, right)
    # Preorder traversal can be used to copy trees
    # Use helper to avoid having to pass root node to method call
        def _preorder(root):
            if root:
                print(root.key, end=' ')
                _preorder(root.left)
                _preorder(root.right)         
        _preorder(self.root)
        
    def inorder(self):
    # Print tree in inorder traversal (left, root, right)
    # Inorder traversal gives nodes in non-decreasing order
    # Use helper to avoid having to pass root node to method call
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.key, end=' ')
                _inorder(root.right)
        _inorder(self.root)
        
    def postorder(self):
    # Print tree in postorder traversal (left, right, root)
    # Postorder traversal can be used to delete trees
    # Use helper to avoid having to pass root node to method call
        def _postorder(root):
            if root:
                _postorder(root.left)
                _postorder(root.right)
                print(root.key, end=' ')
        _postorder(self.root)
            
    def insert(self, key):
        # New keys are always inserted after a leaf node
        # We search recursively for the key we are inserting until we reach 
        # a leaf node. The key is inserted as a child of the leaf node
        
        if self.root is None:   # If tree is empty 
            self.root = Node(key)
        else:
            parent = self.root
            while parent:
                if key < parent.key:            # Go left
                    if parent.left is None:     # If left is empty, insert node here
                        parent.left = Node(key)
                        break
                    parent = parent.left        # If left not empty, continue left
                elif key > parent.key:          # Go right
                    if parent.right is None:    # If right empty, insert node
                        parent.right = Node(key)
                        break
                    parent = parent.right       # If not empty, continue right
                else:                           # If equal to parent, node already in tree. Do not insert (no duplicate nodes)
                    print("The value you are trying to insert already exists in the tree")
                    break
                

                    
    def insert_rec(self, key):
        return
        
        
  
  
myTree = Tree()

myTree.insert(10)
myTree.insert(3)
myTree.insert(12)
myTree.insert(4)
myTree.insert(9)

myTree.preorder()
print()
myTree.inorder()
print()
myTree.postorder()
