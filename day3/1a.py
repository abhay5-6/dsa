# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal(self, root):
        inorder = []
        preorder = []
        postorder = []

        def dfs(node):
            if node is None:
                return

            preorder.append(node.data)

            dfs(node.left)

            inorder.append(node.data)

            dfs(node.right)

            postorder.append(node.data)

        dfs(root)

        return preorder, inorder, postorder
