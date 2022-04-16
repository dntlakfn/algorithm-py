arr = [5,9,7,8,1,2,0,44,77,5,17,35,13,10]

# insertion sort
for i in range(1, len(arr)):
    if arr[i] >= arr[i-1]:
        continue
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
print(arr)