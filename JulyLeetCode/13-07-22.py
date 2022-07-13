# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        while queue:
            height, level = len(queue), 0
            temp = []
            while level < height:
            # print(front.val)
                front = queue.popleft()
                temp.append(front.val)
                if front.left != None:
                    queue.append(front.left)
                if front.right != None:
                    queue.append(front.right)
                level +=1
            ans.append(temp)
        return ans