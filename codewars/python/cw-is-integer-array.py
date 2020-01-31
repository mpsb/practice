from decimal import Decimal

def is_int_array(arr):
    if arr == []:
        return True
    elif isinstance(arr, list) == True: # check if input is list
        result = True
        
        for i in arr: # check each element whether they're a number. if they are, then check how many decimal places
            if isinstance(i, (int,float)) == False:
                result = False
                break
            elif Decimal(str(i)).as_tuple().exponent <= -1: # check for how many decimal places
                if str(i)[::-1][0] == '0':
                    continue
                else:
                    result = False
                    break

        return result
    else:
        return False