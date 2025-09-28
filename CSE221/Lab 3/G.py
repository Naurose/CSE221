#G #220 Trees
import sys
class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        value = preorder[0]
        node = TreeNode(value)
        node_index = inorder.index(value)

        node.left = self.build_tree(preorder[1:node_index + 1], inorder[:node_index])
        node.right = self.build_tree(preorder[node_index + 1:], inorder[node_index + 1:])
        return node

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.elem, end=' ')

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().split()))
preorder = list(map(int, sys.stdin.readline().split()))

tree = BinaryTree()
tree.root = tree.build_tree(preorder, inorder)
tree.post_order(tree.root)