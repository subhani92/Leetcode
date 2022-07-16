# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        """root is first element of preorder"""
        root = TreeNode(preorder[0])
        """fins the index of root in inorder array"""
        try:
            index_of_root = inorder.index(preorder[0])
        
            root.left = self.buildTree(preorder[1:index_of_root+1], inorder[:index_of_root])
            root.right = self.buildTree(preorder[index_of_root+1:], inorder[index_of_root+1:])

            return root
        except:
            pass
