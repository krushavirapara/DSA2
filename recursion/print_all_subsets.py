def print_all_subsets(ip,op):
    if len(ip)==0:
        print(op)
        return
    op1 =  op
    op2 = op + ip[0]
    ip = ip[1:]
    print_all_subsets(ip,op1)
    print_all_subsets(ip,op2)

print_all_subsets("abc","")
