# TO-DO: Complete the selection_sort() function below 


# assume that the first index is the smallest
# then compare to the next index (Loops)
# if next index is smaller it is now the smallest
# then swap so that smaller index come before larger index
# Do this until all are order
# this is 0(n^2)

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # loc is line of code
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                 smallest_index = j          
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
# 0(n^2)
# this goes one by one comparing a num to another (Loops)
def bubble_sort( arr ):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i] 
        
    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr