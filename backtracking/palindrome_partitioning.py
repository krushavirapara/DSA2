# Python implementation
class GFG:

    def checkPalindrome(self, s):
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, res, s, ind, curr):
        if ind == len(s):
            li = curr.split(",")
            print(li)
            res.append(list(li[1:]))
            return

        temp = ""
        for i in range(ind, len(s)):
            left = s[ind:i+1]
            if self.checkPalindrome(left):
                new = curr + "," +  left
                self.partition(res, s, i + 1, new)
                
                

    def main(self):
        obj = GFG()
        res = []
        s = ""
        ind = 0
        curr = []
        obj.partition(res, s, ind, "")

        for iter in res:
            print(iter)

# Creating an instance of GFG class
gfg_obj = GFG()
gfg_obj.main()
