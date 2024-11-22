#time o(n) n include all element in array and sub array
def power_integer(arr , pow = 1):
    sum = 0 
    for i in arr:
        if type(i) == list:
            sum += power_integer(i, pow+1)
        else:
            sum += i
    return sum**pow
print(power_integer([1,2,[3 , 4],[[2]]]))