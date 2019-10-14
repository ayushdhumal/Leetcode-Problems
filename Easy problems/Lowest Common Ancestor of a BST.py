# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            #In a BST, if a value is less than the rot node, it is on the left
            if(p.val < root.val > q.val):
                return self.lowestCommonAncestor(root.left, p, q)
            #In a BST, if a value is less than the rot node, it is on the left
            elif(p.val>root.val<q.val):
                return self.lowestCommonAncestor(root.right,p,q)
            #If not above 2 cases, we have already found our lowest common ancestory
            else:
                return root
        
