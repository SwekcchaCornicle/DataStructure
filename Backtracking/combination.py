# time = no of nodes * no of work done at each node  k *nck space o(k)
# def combine(n,k):
#     #write code here
#     res = []
#     ex = list(range(n))
#     print(ex)
#     def helper(start,cx):  
#         if len(cx) == k:
#             print(cx)
#             res.append(cx.copy())
#             return
#         for i in range(start,len(ex)):
#             cx.append(ex[i])
#             helper(i+1,cx) 
#             cx.pop()
#     helper(0,[])
#     return(res)
# combine(3,2)


# time = no of nodes * no of work done at each node  k *nck space o(k)
def combine(n,k):
    #write code here
    res = []
    ex = list(range(n))
    print(ex)
    def helper(start,cx):  
        if len(cx) == k:
            print(cx)
            res.append(cx.copy())
            return
        need = k-len(cx)
        for i in range(start,n-(need -1)):
            cx.append(ex[i])
            helper(i+1,cx) 
            cx.pop()
    helper(0,[])
    return(res)
combine(3,2)
        