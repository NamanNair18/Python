def reverse (start, end, arr):
    no_of_reverse = end-start+1

    count = 0
    while((no_of_reverse)//2 != count):
        arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
        count += 1
    return arr

def left_rotate_arr(arr, size, d):
     # Reverse the Entire List
    start = 0
    end = size - 1
    arr = reverse(start, end, arr) 
   
    # Divide array into twosub-array based on no of rotations. 
    start = 0
    end = size - d - 1
    arr = reverse(start, end, arr) 
    
    # Divide Second sub-array Reverse the Second sub-array
    start = size - d
    end = size - 1
    arr = reverse(start, end, arr)
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
size = 8
d = 1
print('The Original array: ', arr)

# Finding all the symmetric rotation number
if ( d<= size):
    print("The Rotated Array:- ", left_rotate_arr(arr, size, d))

else:
    d = d % size
    print('Rotated array: ', left_rotate_arr(arr, size, d))