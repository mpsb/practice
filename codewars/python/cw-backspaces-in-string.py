def clean_string(s):
    a = []
    for i in s:
        if i == '#':
            if len(a) == 0:
                continue
            else:
                a.pop(-1)
        else:
            a.append(i)
    
    return ''.join(a)