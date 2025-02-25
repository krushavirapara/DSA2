class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        reverse = False
        while queue:
            size = len(queue)
            ans = []
            ab=[i.val for i in queue]
            print(ab)
            for i in range(size):
                if not reverse:
                    temp = queue.pop(0)
                    ans.append(temp.val)
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
                else:
                    temp = queue[-1]
                    queue.remove(temp)
                    ans.append(temp.val)
                    if temp.right:
                        queue.insert(0,temp.right)
                    if temp.left:
                        queue.insert(0,temp.left)
                    
            reverse = not reverse
            res.append(ans)
        return res
        