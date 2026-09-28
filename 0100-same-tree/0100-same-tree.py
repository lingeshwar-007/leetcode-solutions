# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def check(le, ri):
            if le==None and ri==None:
                return True
            if le==None or ri==None:
                return False
            if le.val!=ri.val:
                return False
            left=check(le.left, ri.left)
            right=check(le.right, ri.right)
            return left and right
        return check(p, q)
        