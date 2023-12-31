# Preorder travesal solved iteratively
# Needs to build a binary tree for this code to work

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        curr, stack  = root, [] 
        res = []


        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()


root = [1,None,2,3]

a = Solution()
a.preorderTraversal(root)