# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
    #Getting the value of nodes in an ascending way(inorder traversal) and storing 'em in an array
        def inorder(root):
            if root:
                inorder(root.left)
                vals.append(root.val)
                inorder(root.right)
        vals = []
        inorder(root)
    #Once stored, popping each element and summing it with the surrent value of sums
        self.sums = 0
        def reverseorder(root):
            if root:
                reverseorder(root.right)
                self.sums += vals.pop()
                root.val = self.sums
                reverseorder(root.left)
        reverseorder(root)

        return root
