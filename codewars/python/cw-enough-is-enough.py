'''
Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

Task
Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
'''

from collections import Counter

def delete_nth(order,max_e):
    value_counts = Counter(order) # value counts of order
    bigger_than = []
    
    for i in value_counts: # store all values in bigger_than that's greater than max_e
        if value_counts[i] > max_e:
            bigger_than.append(i)
    
    value_counts = Counter({i:0 for i in value_counts}) # reset all zeros as counter for order
    
    for i,e in enumerate(order): # replace values to be removed in order with None values
        if e in bigger_than:
            value_counts[e] += 1
        if value_counts[e] > max_e:
            order[i] = None
    
    order = list(filter(lambda a: a != None, order)) # filter out all None values

    return order