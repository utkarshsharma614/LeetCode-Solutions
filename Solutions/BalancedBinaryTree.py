# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(node):
            if not node:
                return (0, True)
            
            left_height, left_balanced = helper(node.left)
            right_height, right_balanced = helper(node.right)
            
            return (max(left_height, right_height) + 1, left_balanced and right_balanced and abs(left_height - right_height) <= 1)
        
        return helper(root)[-1]