'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
'''

def check_even(list):
    even_count = 0
    odd_count = 0
    
    for i in list:
        i = int(i)
        if(i % 2 == 0):
            even_count += 1
        else:
            odd_count += 1
        if(even_count > 1):
            return True
        if(odd_count > 1):
            return False
    
def iq_test(numbers):
    num_list = list(numbers.split(' '))
    counter = 1
    is_even = check_even(num_list) # to check whether list majority is even or odd
    
    if(is_even):
        for i in num_list:
            i = int(i)
            if(i % 2 != 0):
                return counter
            counter += 1
    else:
        for i in num_list:
            i = int(i)
            if(i % 2 == 0):
                return counter
            counter += 1