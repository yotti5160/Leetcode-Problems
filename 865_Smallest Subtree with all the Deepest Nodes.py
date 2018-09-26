class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def help(node, dep):
            if not node:
                return None, dep-1
            nl, dl=help(node.left, dep+1)
            nr, dr=help(node.right, dep+1)
            if dl>dr:
                return nl, dl
            if dr>dl:
                return nr, dr
            return node, dl
            
        node, dep=help(root, 1)
        return node
