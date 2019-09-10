'''
The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.

In effect: 89 = 8^1 + 9^2

The next number in having this property is 135.

See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
'''

def calc(number): # calculate number using exponential property
    num_list = list(str(number))
    exponential = 1
    answer = 0
    counter = 0
    
    for i in num_list: # convert list of strings to integers
        num_list[counter] = int(i)
        counter += 1

    for i in num_list: # calculate equation
        answer += i**exponential
        exponential += 1
    
    return answer

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    input_range = range(a,b+1)
    output_range = []
    
    for i in input_range:
        answer = calc(i)
        
        if(answer == i): # check whether integer fits eureka property
             output_range.append(i)           

    return output_range