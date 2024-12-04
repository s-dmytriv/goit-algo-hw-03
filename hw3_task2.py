import random

def get_numbers_ticket(min, max, quantity):
        if (min < 1 or max > 1000 or max < min):
            return "Invalid range"
        if (quantity > (max-min+1) or quantity < 1):
            return "Invalid quantity"
        else:    
            numbers = random.sample(range(min,max+1), quantity)
        return sorted(numbers)

lottery_numbers = get_numbers_ticket(10,50,7)

if isinstance(lottery_numbers, list):
    print(f"Your lottery numbers are {lottery_numbers}.")
else:    
    print(f"ERROR: {lottery_numbers}") 

