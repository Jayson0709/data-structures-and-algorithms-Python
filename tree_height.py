class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree_height(self, root):
        # write code here
        ans = 0
        if root == None:
            return ans
        left = self.tree_height(root.left);
        right = self.tree_height(root.right);
        return max(left, right) + 1
