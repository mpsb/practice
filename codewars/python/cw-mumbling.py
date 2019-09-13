'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
'''
def accum(s):
    s_list = list(s.upper()) 
    new_list = []
    dash = "-"
    counter = 0
    
    for i in s_list:
        new_list.append(i)
        new_list.append(i.lower()*counter)
        if(counter == len(s)-1): # last loop doesn't need a dash at the end
            break
        new_list.append(dash)
        counter += 1

    return "".join(new_list)