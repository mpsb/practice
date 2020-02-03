def exchange_with(a, b):
    c = b.copy()
    b[:] = a.copy() # needed to add [:] to update the contents outside the function. without it, a and b only updates locally (inside the function)
    a[:] = c
    
    a.reverse()
    b.reverse()