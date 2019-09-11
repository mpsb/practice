'''
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
'''

def diamond(n):
    if((n%2==0) | (n<0)):
        return None
    
    space = " "
    asterisk = "*"
    newline = "\n"
    diamond = ""
    space_num = int(1*n/2)
    asterisk_num = 1

    for i in range(int(n/2)+1): # top part
        diamond += space*space_num
        diamond += asterisk*asterisk_num
        diamond += newline
        space_num -= 1
        asterisk_num += 2
    
    space_num += 2
    asterisk_num -= 4
    
    for i in range(int(n/2)+1): # bottom part
        if(asterisk_num <= 0):
            break
        diamond += space*space_num
        diamond += asterisk*asterisk_num
        diamond += newline
        space_num += 1
        asterisk_num -= 2
        
    return diamond