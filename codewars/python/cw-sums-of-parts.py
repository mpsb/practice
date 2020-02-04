def parts_sums(ls):
    result = [0]
    sum = 0
    
    ls.reverse()
    
    for i in ls:
        sum += i
        result.append(sum)
        
    result.reverse()
    
    return result