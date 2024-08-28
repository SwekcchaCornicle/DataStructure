position = int(input("position of rotation"))
arr = [5 , 6 ,9 ,8 ,7]
new_arr = arr[position:len(arr)] + arr[0:position]
print(new_arr)
