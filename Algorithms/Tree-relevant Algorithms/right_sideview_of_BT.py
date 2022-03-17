# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def right_sideview(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            '''
            1. 如果是层序遍历所有的结点，变成result.append([node.val for node in queue])即可
            2. 如果是要反向遍历，最后的返回值变成result[::-1]即可
            3. 如果是要返回左视图，变成result.append([node.val for node in queue][0])即可
            '''
            result.append([node.val for node in queue][-1])
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return result
