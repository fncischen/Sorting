# TO-DO: Complete the selection_sort() function below 
def insertion_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # print("We are at index", i )
        cur_index = i

        # copy the item at the index into the temp variable 
        smallest_index = cur_index
        # TO-DO: find next smallest element

        # (hint, can do in 3 loc) 
        # print("Compare:", arr[cur_index], arr[cur_index+1])
        # print("Before:", arr)
        if arr[cur_index] > arr[cur_index+1]:
            
            largerItem = arr[cur_index]
            smallerItem = arr[cur_index+1]
            
            # move the 2nd item, which is smaller, to the 1st. 
            arr[cur_index+1] = largerItem
            arr[cur_index] = smallerItem 

            # print("Check to go backwards", arr[cur_index - 1] , arr[cur_index])

            if (arr[cur_index - 1] > arr[cur_index]) & (cur_index - 1  >= 0):
                for i in range(smallest_index,0,-1):


                    largerItem = arr[i]
                    smallerItem = arr[i-1]

                    # print("Going backwards", smallerItem,largerItem)
                    # print("Going backwards array", arr)
                    if arr[i-1] > arr[i]:
                        arr[i-1] = largerItem
                        arr[i] = smallerItem

        # print(arr)

    return arr

e = [1,5,2,1,1]
k = [8,5,1,9,2]
p = [9,8,1,3,2]
print(insertion_sort(e))
print(insertion_sort(k))
print(insertion_sort(p))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr