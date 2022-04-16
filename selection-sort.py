arr = [5,9,7,8,1,2,0,44,77,5,17,35,13,10]

# selection sort
for i in range(len(arr)):
    m = i
    for j in range(i+1, len(arr)):
        if arr[m] > arr[j]:
            m = j
    arr[i], arr[m] = arr[m], arr[i]
print(arr)