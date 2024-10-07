array =  [-3 , 1, 2,7]

#brute force array: squared each element in array and put each elemant in new element and use any sorting allgo - time-o(nlogn)+n space-o(n)

#2nd method time-o(n) spacce-o(n)
i = 0
j = len(array) - 1
new_array = [0] * len(array)
for k in reversed(range(len(array))):
    sq_i = array[i]**2
    sq_j = array[j]** 2
    if sq_i > sq_j:
        new_array[k] = sq_i
        i += 1
    else:
        new_array[k] = sq_j
        j -= 1
print(new_array)