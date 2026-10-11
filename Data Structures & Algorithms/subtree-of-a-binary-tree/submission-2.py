# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot  or root and not subRoot:
            return False
        if self.sameTree(root, subRoot) == True:
            return True
        else:
           return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
       
        return False
    def sameTree(self, r, sr):
        if not r and not sr:
            return True
        if r and sr:
            if r.val == sr.val:
                return self.sameTree(r.left, sr.left) and  self.sameTree(r.right, sr.right)
                
        return False 