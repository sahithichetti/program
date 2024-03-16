class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        right_height = check_height(node.right)
        # If the subtree is unbalanced or the tree itself is unbalanced, return -1
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        # Otherwise, return the height of the subtree
        return 1 + max(left_height, right_height)

    return check_height(root) != -1

# Test the function
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)

if is_balanced(root):
    print("The binary tree is balanced")
else:
    print("The binary tree is not balanced")
