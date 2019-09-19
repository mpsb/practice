'''
Description:
Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".

Examples
balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
'''

def balance(left, right):
    print(list(left))
    left_counter = 0
    right_counter = 0
    
    for i in list(left):
        if i == '!':
            left_counter += 2
        if i == '?':
            left_counter += 3
    
    for i in list(right):
        if i == '!':
            right_counter += 2
        if i == '?':
            right_counter += 3
    
    if left_counter > right_counter:
        return 'Left'
    elif left_counter < right_counter:
        return 'Right'
    else:
        return 'Balance'