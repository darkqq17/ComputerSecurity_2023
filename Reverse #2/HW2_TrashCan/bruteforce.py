import itertools

def generate_permutations(s):
    # Extract positions and characters of integers in the string
    positions = [i for i, c in enumerate(s) if c.isdigit()]
    digits = [s[i] for i in positions]

    # Generate all permutations of the integers
    permuted_digits = itertools.permutations(digits)

    # Replace integers in the string with each permutation
    results = []
    for perm in permuted_digits:
        # Convert string to list for easy character replacement
        temp_list = list(s)

        # Replace characters at the identified positions
        for pos, char in zip(positions, perm):
            temp_list[pos] = char

        # Convert list back to string and add to results
        results.append(''.join(temp_list))

    return results

# Original string
original_string = "FLAG{S1mpl3_c5N_tras4}"

# Generate permutations
permutations = generate_permutations(original_string)

# Print the results
for p in permutations:
    print(p)
