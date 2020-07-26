from tree_node import TreeNode
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return
        root = TreeNode(preorder[0])#先根
        idx = inorder.index(preorder[0])#中
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root

if __name__ == '__main__':
    a = Solution()
    print(a.buildTree([3,9,20,15,7],[9,3,15,20,7]))