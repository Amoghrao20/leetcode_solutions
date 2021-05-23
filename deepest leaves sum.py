# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Function to get the height of tree
        def getHeight(root):
            if root is None:
                return -1
            else:
                lheight = getHeight(root.left)
                rheight = getHeight(root.right)
                return 1 + max(lheight, rheight)
         
		 #  get height of input tree
        h = getHeight(root)
        
		# function to get to the last level and maintain the sum
        def lastLevel(root, level, sum_):
            if level == 1:
                sum_ += root.val
                return sum_
            else:
                if root.left is not None:
                    sum_ = lastLevel(root.left, level-1, sum_)
                if root.right is not None:
                    sum_ = lastLevel(root.right, level-1, sum_)
            return sum_
        
		# Main driver logic
        if root is None:
            return
        else:
            leavesSum = lastLevel(root, h+1, 0)
        return leavesSum
