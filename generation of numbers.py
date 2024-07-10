import random

def generate_random_number():
    
    random_number = random.randint(1, 99)
    return random_number

random_number = generate_random_number()
print(f"Random number between 1 and 99: {random_number}")
