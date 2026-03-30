# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def _invert_node(node):
            if node == None or (node.left == None and node.right == None):
                return(0)

            _invert_node(node.left)
            _invert_node(node.right)
            node.left, node.right = node.right, node.left
        _invert_node(root)
        return(root)