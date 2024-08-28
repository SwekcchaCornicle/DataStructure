k= int(input("position of rotation"))
arr = [1, 3, 5, 7, 9]
for i in range(k):
    new = arr[len(arr)-1 : len(arr)] + arr[0:len(arr)-1]
    arr = new
print(arr)