def wordbreak(s,op,dic):
    if len(s)==0:
        print(op)
        return 
    for i in range(len(s)):
        left = s[0:i+1]
        if left in dic:
            wordbreak(s[i+1:],op + left + " ",dic)
dic  = {"micro","soft","microsoft","is","hi","ring","hiring"}
wordbreak("microsoftishiring","",dic)
    