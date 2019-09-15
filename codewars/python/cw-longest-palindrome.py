'''
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.
'''

def longest_palindrome (s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    if len(s) == 2:
        s_list = list(s)
        if s_list[0] == s_list[1]:
            return 2
        else:
            return 1
    if len(s) == 3:
        s_list = list(s)
        if s_list[0] == s_list[2]:
            return 3
        elif (s_list[0] == s_list[1]) | (s_list[1] == s_list[2]):
            return 2
        else:
            return 1
    
    s_list = list(s)
    max_length = 1
    curr_length = 0
    lower = 0
    even_upper = 1
    odd_upper = 2
    is_even = True
    
    for i,e in enumerate(s_list):
        if i == len(s_list)-2:
            if max_length < curr_length:  
                max_length = curr_length
            break
        if i-lower < 0:
            lower = 0
        if s_list[i-lower] == s_list[i+even_upper]: # check for even palindromes 
            curr_length += 2
            lower += 2
        elif s_list[i-lower] == s_list[i+odd_upper]: # check for odd palindromes
            is_even = False
            curr_length += 2
            lower += 2
        else:
            lower = 0
            if max_length < curr_length:  
                max_length = curr_length
            curr_length = 0
    
    if is_even:
        return max_length
    else:
        max_length += 1
        return max_length

    return max_length