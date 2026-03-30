# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def _depth(node, depth):
            if node == None:
                return(depth)
            depth += 1
            return(max( _depth(node.left, depth), _depth(node.right, depth)))
        
        return(_depth(root, 0))
