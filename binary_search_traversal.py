"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
  
"""


[
    [1],
    [2,3],
    [4,5,6,7]
]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# queue = [2,3], next_queue = [4,5], level =[2]; result=[[1]]
## [1,2,3,4,5,6,7]
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        next_queue =[]
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.level is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result

loop 1:
queue = [2,3], next_queue =[] , level =[]; result=[[1]]
loop 2 :
queue = [4,5,6,7], next_queue =[] , level =[]; result=[[1],[2,3]]
loop 3 : because there is no children anymore so add queue to result
queue = [], next_queue =[] , level =[]; result=[[1],[2,3],[4,5,6,7]]











        
