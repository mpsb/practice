'''
The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
'''

def remove_smallest(numbers):
    num_length = len(numbers)
    if((num_length == 1) | (numbers == [])):
        return []
    
    new_numbers = numbers.copy() # copy to avoid input mutations
    smallest_int = 0
    comp_int = 0
   
    for i in range(num_length):
        if(i == 0):
            smallest_int = numbers[i]
            continue
        comp_int = numbers[i]
        if(comp_int < smallest_int):
            smallest_int = numbers[i]
    
    new_numbers.remove(smallest_int)