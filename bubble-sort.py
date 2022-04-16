arr = [5,9,7,8,1,2,0,44,77,5,17,35,13,10]

# bubble sort
for i in range(len(arr)):
    swap = False
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True
    if swap == False:
        break
print(arr)