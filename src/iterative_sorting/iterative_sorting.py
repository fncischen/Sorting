# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i

        # copy the item at the index into the temp variable 
        smallest_index = cur_index
        # TO-DO: find next smallest element

        # (hint, can do in 3 loc) 
        if arr[cur_index] > arr[cur_index+1]:
            
            largerItem = arr[cur_index]
            smallerItem = arr[cur_index+1]
            
            # move the 2nd item, which is smaller, to the 1st. 
            arr[cur_index+1] = largerItem
            arr[cur_index] = smallerItem 

            if (arr[cur_index - 1] > arr[cur_index]) & (cur_index - 1  > 0):
                for i in range(smallest_index,0,-1):

                    largerItem = arr[i]
                    smallerItem = arr[i-1]

                    if arr[i-1] > arr[i]:
                        arr[i-1] = largerItem
                        arr[i] = smallerItem

    return arr

e = [1,5,2,1,1]
k = [8,5,1,9,2]
print(selection_sort(e))
print(selection_sort(k))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr