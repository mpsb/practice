def maxSequence(arr):
    if arr == []:
        return 0
    
    is_neg = False
    # check if array has negative numbers
    for i in arr:
        if(i < 0):
            is_neg = True
            break
    
    if is_neg == False:
        return sum(arr)
    else:
        arr_copy = arr.copy()
        max_value = 0
        
        for i,e in enumerate(arr):
            starting_index = i+1
            for j in arr_copy[starting_index:]:
                e += j

                if e > max_value:
                    max_value = e
        
        return max_value