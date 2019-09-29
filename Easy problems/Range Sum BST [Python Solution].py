# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        #If the root does not exist, return sum as 0
        if not root:
            return 0
        #Storing the sum in the result variable
        result = 0
        if L <= root.val <= R:
            result += root.val
        #Traversing trough the left subtree to find the sum
        if L <= root.val:
            result += self.rangeSumBST(root.left, L, R)
        #Traversing through the right sub tree tofind the sum
        if R > root.val:
            result += self.rangeSumBST(root.right, L, R)
        return result
