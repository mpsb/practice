'''
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
'''
def expanded_form(num):
    str_num = str(num)
    str_num_len = len(str_num)
    answer = ""
    
    for i in range(str_num_len):
        if str_num_len == 1:
            if str_num[i] == "0":
                answer = answer[:-3]
                break
            else:
                answer += str_num[i]
                break
        if str_num[i] == "0":
            str_num_len -= 1
        else:
            answer += str_num[i] + "0"*(str_num_len-1)
            answer += " + "
            str_num_len -= 1

    return answer