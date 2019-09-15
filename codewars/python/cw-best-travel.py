'''
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible

to please Mary and John- ?
Example:

With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language. With C++, C, Rust, Swift, Go, Kotlin return -1.
'''

import itertools

def choose_best_sum(t, k, ls):
    print(t, k, ls)
    if len(ls) < k:
        return None
    else:    
        ls.sort(reverse=True)
        new_ls = [i for i in ls]
        
        # preliminary elimination
        for i in new_ls:
            if (i == t) & (k == 1): # just in case
                return i
            if i > t:
                new_ls.remove(i)
            
        comb_list = list(itertools.combinations(new_ls, k))
        sum_list = [sum(i) for i in comb_list]
        
        sum_list.sort()
        
        max_sum = 0
        
        for i in sum_list:
            print(i, t)
            if i > t:
                break
            if i == t: # just in case
                return i
            if max_sum < i: 
                max_sum = i
        
        if max_sum == 0:
            return None
        else:
            return max_sum