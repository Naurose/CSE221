#H #Trees Reassessed 
import sys
class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        value = postorder[-1]
        node = TreeNode(value)
        node_index = inorder.index(value)

        node.left = self.build_tree(inorder[:node_index], postorder[:node_index])
        node.right = self.build_tree(inorder[node_index + 1:], postorder[node_index:-1])
        return node

    def preorder(self, node):
        if node is not None:
            print(node.elem, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

tree = BinaryTree()
tree.root = tree.build_tree(inorder, postorder)
tree.preorder(tree.root)