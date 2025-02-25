
class Node:
    def __init__(this,data):
        this.data = data
        this.left = None
        this.right = None
    
pre_arr = [50,25,12,None,None,37,30,None,None,None,75,62,None,70,None,None,87,None,None]

i = 0

root = Node(50)
st = [[root,1]]
i=1

while st:
    top,state = st[-1]
    if state == 1:
        if pre_arr[i]:
            top.left = Node(pre_arr[i])
            i+=1
            st[-1][1]+=1
            st.append([top.left,1])
        else:
            st[-1][1]+=1
            i+=1
    elif state == 2:
        if pre_arr[i]:
            top.right = Node(pre_arr[i])
            i+=1
            st[-1][1]+=1
            st.append([top.right,1])
        else:
            st[-1][1]+=1
            i+=1
    else:
        st.pop()
        
order = []
def iter_pre(root):
    order=[]
    inorder =[ ]
    post =[]
    st = [[root,1]]
    while st:
        top,state = st[-1]
        if state==1:
            order.append(top.data)
            if top.left:
                st[-1][1]+=1
                st.append([top.left,1])
            else:
                st[-1][1]+=1
                
        elif state==2:
            inorder.append(top.data)
            if top.right:
                st[-1][1]+=1
                st.append([top.right,1])
            else:
                
                st[-1][1]+=1
                
        else:
            post.append(top.data)
            st.pop()
    print(inorder)
    print(post)
    return order
print(iter_pre(root))
            
        
     