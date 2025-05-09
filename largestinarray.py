def largest(arr, n):
    max=arr[0]
    for i in range(1, n):
        if arr[i] > max: 
            max = arr[i]
    return max

arr=[12, 3, 4, 5, 6, 80]
n=len(arr)
ans =  largest(arr, n)
print("The Largest Elemnt in the Array is :-", ans)

