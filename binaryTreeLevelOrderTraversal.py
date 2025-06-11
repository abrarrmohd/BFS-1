"""
Problem: Binary Tree Level Order Traversal
Approach: Do a BFS traversal and add all the elements of the current level to the result. Can do this 
by tracking the current size of the queue
t.c. => O(n)
s.c. => O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res = []
        if not root:
            return []
        q.append(root)
        
        while q:
            subList = []
            for i in range(len(q)):
                root = q.pop(0)
                subList.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(subList)
        return res