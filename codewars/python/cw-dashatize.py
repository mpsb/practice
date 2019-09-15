'''
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.
'''
def dashatize(num):
    if num == None:
        return 'None'
    elif num == 0:
        return str(num)        
    else:
        num_list = [i for i in str(num)]

        if num_list[0] == "-":
            num_list.pop(0)

        if len(num_list) == 1:
            return str(num_list[0])
        else:
            num_list = [int(i) for i in num_list]
            counter = 0
            for i in num_list:
                if (num_list[counter]%2 != 0) & (counter == len(num_list)-1):
                    if num_list[counter-1] == "-":
                        num_list[counter] = str(num_list[counter])
                        break
                    else:
                        num_list[counter] = str(num_list[counter])
                        num_list.insert(len(num_list)-1, "-")
                        break
                elif(counter >= len(num_list)-1):
                    num_list[counter] = str(num_list[counter])
                    break
                elif (num_list[counter]%2 != 0) & (counter == 0):
                    num_list[counter] = str(num_list[counter])
                    num_list.insert(1, "-")
                    counter += 1
                elif num_list[counter]%2 != 0:
                    num_list[counter] = str(num_list[counter])
                    if num_list[counter-1] == "-":
                        num_list.insert(counter+1, "-")
                        counter += 1
                    else:
                        num_list.insert(counter, "-")
                        num_list.insert(counter+2, "-")
                        counter += 2
                num_list[counter] = str(num_list[counter])
                counter += 1

            return "".join(num_list)