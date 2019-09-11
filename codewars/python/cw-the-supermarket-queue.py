'''
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.
'''

def get_dict_max(dict, n):
    max = 0
    for i in range(n):
        if(max < sum(dict.get(i))):   
            max = sum(dict.get(i))
    return max

def get_dict_min_index(dict, n):
    min = sum(dict.get(0))
    index = 0
    for i in range(n):
        if(min > sum(dict.get(i))):   
            min = sum(dict.get(i))
            index = i
    return index

def queue_time(customers, n):
    customer_len = len(customers)
    
    if(customer_len == 0): # no customers, no time spent
        return 0 
    elif(n == 1): #if one queue, sum of customers list
        return sum(customers)
    elif((customer_len <= n)): # get max if number of tills is less than or equal to number of customers
        return max(customers) 
    else: 
        total_time = 0
        queues = {}
        min_current_index = 0
        
        for i in range(n): # create lists according to number of tills to store values
            queues[i] = [0]
        
        for i in customers: #create queues
            min_current_index = get_dict_min_index(queues, n) # determine which queue is available for i by finding minimum amount of time spent for all queues at the time
            queues[min_current_index].append(i)
        
        total_time = get_dict_max(queues, n) # total time spent is max time spent among all tills

        return total_time
    