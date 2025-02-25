#leetcode 637
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res =[]
        queue = [root]

        while queue:
            size=len(queue)
            ans=[]
            for i in range(size):
                temp = queue[0]
                queue.remove(temp)
                ans.append(temp.val)
                if temp.left:
                     queue.append(temp.left)
                if temp.right:
                     queue.append(temp.right)
            res.append(sum(ans)/size)
        return res