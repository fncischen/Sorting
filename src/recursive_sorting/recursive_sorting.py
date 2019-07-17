# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    i = 0

    aIndex = 0
    bIndex = 0

    while len(arrA) and len(arrB):
        print(aIndex, bIndex)
        if arrA[aIndex] > arrB[bIndex]:
            merged_arr[i] = arrB[bIndex]
            arrB.pop(bIndex)
            aIndex += 1 
        else:
            merged_arr[i] = arrA[aIndex]
            arrA.pop(aIndex)
            bIndex += 1  
        i += 1

    if len(arrA):
        for p in range(len(arrA)):
            merged_arr[i] = arrA[p]
            i += 1
    elif len(arrB):
        for p in range(len(arrB)): 
            merged_arr[i] = arrB[p]
            i += 1      
                
    return merged_arr

# before
# [1,5,9] [2,3,5]

# after merge
# [1,5,9, 2,3,5]

# after merge sort
# [1,2,3,5,5,9]

# a1 = [1,5,9]
# a2 = [2,3,5]

# print(merge(a1,a2))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1:
        return arr
    # grab two pieces at a time and swapping as needed
    # You lay out all the contents on a table, grabbing two pieces at a time, placing the older document on top of the newer one. 
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0] , arr[1] = arr[1], arr[0]
            return arr
    if len(arr) > 2:

        # Then, you start merging sorted sets of documents together until the folder is done.
        a1 = arr[0:int(len(arr)/2)]
        a2 = arr[(int(len(arr)/2)):len(arr)]

        a1 = merge_sort(a1)
        a2 = merge_sort(a2)

        # Once all the folders have been reassembled, you order the folders correctly in the drawer. 
        mergedArr = merge(a1,a2)

        return mergedArr


    return arr

print(merge_sort([1,5,9,2,3,5]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
