# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        left_side = []
        if not root:
            return []
    
        self.dfs(root, left_side, 0 )        
        return left_side
        
        
    def dfs(self, root, left_side, level):
        if not root:
            return 
        
        if level == len(left_side):
            left_side.append(root.val)
        
        self.dfs(root.right, left_side,level+1)
        self.dfs(root.left, left_side,level+1 )
        