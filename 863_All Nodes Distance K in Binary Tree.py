class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        #Turn the binary tree into two dictionaries.
        #upward(dict) gives the value of its parent node.
        #downward(defaultdict(list)) gives the values of its child nodes.
        #visited(dict) is for BFS.
        upward, downward, visited={}, collections.defaultdict(list), {}
        def run(root):
            if not root:
                return
            visited[root.val]=False
            if root.left:
                downward[root.val].append(root.left.val)
                upward[root.left.val]=root.val
                run(root.left)
            if root.right:
                downward[root.val].append(root.right.val)
                upward[root.right.val]=root.val
                run(root.right)
        run(root)

        ret=[]
        def bfs(distance, nodeVal):
            visited[nodeVal]=True
            if distance==K:
                ret.append(nodeVal)
                return
            #search down
            for node in downward[nodeVal]:
                if not visited[node]:
                    bfs(distance+1, node)
            #search up
            if nodeVal in upward and not visited[upward[nodeVal]]:
                bfs(distance+1, upward[nodeVal])
            return

        bfs(0, target.val)
        return ret 
