# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root: 
            return True
        #If left node exists
        if root.left:
            if root.val != root.left.val:
                return False
        #If right node exists
        if root.right:
            if root.val != root.right.val:
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
   
