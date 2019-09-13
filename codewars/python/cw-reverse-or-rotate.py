'''
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
'''

import textwrap

def rotate(string):
    string_list = list(string)
    return "".join(string_list[1:] + string_list[:1])

def revrot(strng, sz):
    if(sz <= 0) | (sz == "") | (sz > len(strng)):
        return ""
    
    strng_list = textwrap.wrap(strng, sz) # chunking
    bool_list = []
    loop_string = ""
    loop_list = []
    result = ""
    
    for i, ele in enumerate(strng_list):
        loop_list = list(ele) # convert chunk to a list
        loop_list = map(int, loop_list) # convert each string in list to ints
        
        if sum(loop_list)%2 == 0: # no need to check for cubes of digits as cubes of even numbers are always even and vice-versa
            bool_list.append(True)
        else:
            bool_list.append(False)
    
    for i, ele in enumerate(strng_list):
        if len(ele) < sz: # omit chunk from result if less than sz
            break

        if bool_list[i] == True: # no need to check for cubes of digits as cubes of even numbers are always even and vice-versa
            loop_string = ele[::-1]
        else:
            loop_string = rotate(ele)
        
        result += loop_string

    return result