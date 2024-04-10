import random

def get_numbers_ticket(min, max, quantity):
    '''
    This function generates a set of unique random numbers for lotteries.
    '''
    # Checking the correctness of input data
    if not (1 <= min <= max <= 1000) or max - min < quantity:
        return[] 
        
    # Use set to ensure uniqueness of numbers
    numbers = set()
    
    # Generation of unique numbers
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
        
    # Return a sorted list of unique numbers
    return sorted(list(numbers)) 

# For example 
lottery_numbers = get_numbers_ticket(10, 15, 5)
print(f'Your lottery numbers is:{lottery_numbers}') 

