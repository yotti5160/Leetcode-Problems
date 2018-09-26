class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dep(node, d):
            if not node:
                return d-1
            return max(dep(node.left, d+1), dep(node.right, d+1))
        return dep(root, 1)   
