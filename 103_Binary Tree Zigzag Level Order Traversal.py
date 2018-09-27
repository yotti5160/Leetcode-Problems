class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret=[]
        up, down, count=[root], [], 1
        while up:
            tmp=[]
            if count%2==1:
                for u in up:
                    tmp.append(u.val)
                    if u.left:
                        down.append(u.left)
                    if u.right:
                        down.append(u.right)
            else:
                for u in up[::-1]:
                    tmp.append(u.val)
                    if u.right:
                        down.insert(0, u.right)
                    if u.left:
                        down.insert(0, u.left)
            ret.append(tmp)
            up, down=down, []
            count+=1
        return ret
