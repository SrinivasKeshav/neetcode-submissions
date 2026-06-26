# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            qlength = len(q)
            temp = []
            for i in range(qlength):
                node = q.popleft()
                if not node:
                    continue
                temp.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if temp:
                res.append(temp)
        return res
