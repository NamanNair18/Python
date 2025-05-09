def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i 
    return(sum)

if __name__ == "__main__":
    arr=[12, 3, 4, 5, 6]
    n=len(arr)
    ans = _sum(arr)
    print('The Sum of the Array is :-', ans)
