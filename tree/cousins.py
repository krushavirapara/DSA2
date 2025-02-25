#leetcode 993
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [(-1,root)]
        res=False
        while queue:
            size = len(queue)
            ans =[]
            for i in range(size):
                temp = queue[0][1]
                queue.remove(queue[0])
                if temp.left:
                    queue.append((temp.val,temp.left))
                if temp.right:
                    queue.append((temp.val,temp.right))
           
            new_x,new_y=0,0
            for i in range(len(queue)):
                if queue[i][1].val==x:
                    new_x = queue[i]
                if queue[i][1].val==y:
                    new_y = queue[i]
            if new_x and new_y:
                if new_x[0]!=new_y[0]:
                    return True
            
        return res
        