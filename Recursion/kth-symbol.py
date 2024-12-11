'''Question 1: k-th symbol in Grammar: We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.'''

# def kt_symbol(n,sym,k):
#     x =''
#     if n == k:
#         for i in sym:
#             if i == '0':
#                 x = x+'01'
#             else:
#                 x=x+'10'
#         return sym
#     for i in sym:
#         if i == '0':
#             x = x+'01'
#         else:
#             x=x+'10'
#     n = n+1
#     return kt_symbol(n,x,k)
# print(kt_symbol(1,'0',4))
# time o(n) , s(n)
# def kgram(n , k):

#     if n ==1:
#         return 0
#     l = pow(2,n-1)
#     half = l // 2
#     if k <= half:
#         return kgram(n-1 , k)
#     else:
#         return int(not kgram(n-1 , k-half))
# print(kgram(3 , 2))

n=int(input())
l=["0","1"]
for i in n:
    if "0" in l:
        "0"="01"
    else:
        "1"="10"
print(l)
    
    
    
