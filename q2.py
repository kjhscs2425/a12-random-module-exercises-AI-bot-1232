import random

# Type of animal (at least 3 choices, string)
animal = random.choice(['dog', 'cat', 'hamster', 'parrot', 'snake'])

# Age (integer)
age = random.randint(1, 15)

# Color (at least 3 choices, string)
color = random.choice(['brown', 'white', 'black', 'gray', 'orange', 'golden'])

# Weight (float)
weight = round(random.uniform(1.0, 50.0), 1)

# Print a summary of your pet using an f-string
print(f"Your pet is a {age}-year-old {color} {animal} weighing {weight} pounds.")