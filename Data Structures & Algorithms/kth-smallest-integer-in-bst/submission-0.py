# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def inorder(root):
            nonlocal res, k
            if(root == None):
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        print(res)
        return res[k-1]
        