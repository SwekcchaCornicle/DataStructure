#time complexity o(2n) space complexity o(n)
count = 0
def helper(N,fromm,to,aux):

    if N==1:
      
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        return
    helper(N-1,fromm,aux,to)

    print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))

    helper(N-1,aux,to,fromm)
helper(3,'a','b','c')  
