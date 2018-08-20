class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        #Turn the binary tree into two dictionaries.
        #upward gives the value of its parent node.
        #downward gives the values of its child node.
        #visited is for BFS.
        upward, downward, visited={}, {}, {}
        def run(root):
            if not root:
                return
            visited[root.val]=False
            if root.left:
                if root.val in downward:
                    downward[root.val].append(root.left.val)
                else:
                    downward[root.val]=[root.left.val]
                upward[root.left.val]=root.val
                run(root.left)
            if root.right:
                if root.val in downward:
                    downward[root.val].append(root.right.val)
                else:
                    downward[root.val]=[root.right.val]
                upward[root.right.val]=root.val
                run(root.right)
        run(root)

        ret=[]
        def help(distance, nodeVal):
            visited[nodeVal]=True
            if distance==K:
                ret.append(nodeVal)
                return
            #search down
            if nodeVal in downward:
                for node in downward[nodeVal]:
                    if not visited[node]:
                        help(distance+1, node)
            #search up
            if nodeVal in upward:
                if not visited[upward[nodeVal]]:
                    help(distance+1, upward[nodeVal])
            return

        help(0, target.val)
        return ret  
