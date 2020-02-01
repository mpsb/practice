def create_phone_number(n):
    return '(%s%s%s) %s%s%s-%s%s%s%s' % tuple([str(i) for i in n])