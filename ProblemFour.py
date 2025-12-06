import random

def make_random_list():
    # Ask the user for X > 20
    while True:
        X = int(input("Enter an integer greater than 20: "))
        if X > 20:
            break
        else:
            print("Value must be greater than 20. Try again.")

    # Create a list of 10 distinct random integers from 0 to X
    ls = []
    while len(ls) < 10:
        num = random.randint(0, X)
        if num not in ls:   # ensure no duplicates
            ls.append(num)

    return ls


# Example run
print(make_random_list())
