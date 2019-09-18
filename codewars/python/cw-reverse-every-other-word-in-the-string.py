'''
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are apart of the word in this kata.
'''

def reverse_alternate(string):
    split = string.split()
    
    for i,e in enumerate(split):
        if i%2 != 0:
            split[i] = e[::-1]
            
    return " ".join(split)