# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(not root or p == root or q == root):
            return root
        #Traversing through the left sub tree to find p or q
        lca = self.lowestCommonAncestor(root.left, p, q)
        #Traversing through the left sub tree to find p or q
        rca = self.lowestCommonAncestor(root.right, p, q)
        #While coming up (In the recursion), if both the nodes are found, then it is our lowest common ancestor, 
        if(lca and rca):
            return root
        #if not return one whichever one has both the nodes
        return lca or rca
        
