import math

# Define the list of numbers
numbers = [
    114059301025943970552219, 3928413764606871165730, 43566776258854844738105,
    1500520536206896083277, 22698374052006863956975682, 781774079430987230203437,
    573147844013817084101, 483162952612010163284885, 781774079430987230203437,
    70492524767089125814114, 3311648143516982017180081, 83621143489848422977,
    31940434634990099905, 927372692193078999176, 16641027750620563662096,
    83621143489848422977, 1500520536206896083277, 83621143489848422977,
    59425114757512643212875125
]

# Approximation of the Golden Ratio
phi = (1 + math.sqrt(5)) / 2

# Function to estimate the position of a large number in the Fibonacci sequence
def estimate_fibonacci_position(F):
    return round(math.log(F * math.sqrt(5), phi))

# Estimate the positions for the provided numbers
estimated_positions = [estimate_fibonacci_position(number) for number in numbers]

print(estimated_positions)

# Convert the estimated positions to ASCII characters
plaintext = ''.join([chr(position) for position in estimated_positions])

print(plaintext)