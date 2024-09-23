def binyarSearch(arr, key, low, high):
    mid =  low + (high - low) // 2
    if arr[mid] == key:
        return True
    else:
        if arr[mid] > key:
            return binyarSearch(arr, key, 0, mid-1)
        else:
            return binyarSearch(arr, key, mid+1, high)

arr = list(map(int, input().split()))
key = int(input("enter the key"))
if len(arr)%2 == 0:
    if binyarSearch(sorted(arr), key, 0, len(arr)):
        print("element found")
    else:
        print("elemrnt not found")

    
else:
    if binyarSearch(sorted(arr), key, 0, len(arr)-1):
        print("element found")
    else:
        print("elemrnt not found")

