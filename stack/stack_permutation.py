def stack_permuattion(ip,op):
    st = []
    c = 0
    n = len(ip)
    for i in ip:
        st.append(i)
        while st and st[-1]==op[c]:
            st.pop()
            c+=1
            
    if c==n:
        return True
    else:
        return False
print(stack_permuattion([1,2,3],[3,2,1]))