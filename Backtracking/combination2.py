#m is min  value, t is target, max depth of tree t/m, , n is no of candidate
# if there  is tree  which have three node and each node have 3 node > 3^0+3^1....3^n-1>>sn=(rn-1)/r-1
#TIME O(n^T/M+1) SPACE= O(T/M) 
def combinationSum(candidates, target):
    res = []
    def combinationSum(index,curr,currSum):
        if currSum>target:
            return
        if currSum ==target:
            res.append(curr[:])
            return
        for j in range(index,len(candidates)):
            curr.append(candidates[j])   
            combinationSum(j,curr,currSum+candidates[j])
            curr.pop()
    combinationSum(0,[],0)
    return res 
print(combinationSum([2,3,4,7],7))