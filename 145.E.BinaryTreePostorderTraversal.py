
# for this solution we need to keep track of all the nodes that we visited
# for preorder traversal there is no need for that

# Needs to build a binary tree for this code to work but works in leetcode



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        stack = root
        print("Stack", stack)
        visited = [False]
        res = []

        while stack:
            curr = stack.pop()
            print("visited", visited)
            v = visited.pop()
            if curr:
                print("Cuurr", curr.val)
                if v:
                    
                    res.append(curr.val)
                    print("Res" , res)
                    
                else:
                    print("before Stack" , stack)
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
                    print("After Stack" , stack)
                    print("After stack visited", visited)
        return res

# Test case 1
a3 = TreeNode(3,None,None) 
a2 = TreeNode(2,a3,None)
a1 = TreeNode(1,None,a2)


root = [a1,None,a2,a3]

s = Solution()
print("result", s.postorderTraversal(root))