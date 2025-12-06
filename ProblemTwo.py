def even_odd_list():
    # Step 1: Collect 5 integers from the user
    numbers = []
    for i in range(5):
        user_input = int(input(f"Enter integer #{i+1}: "))
        numbers.append(user_input)

    # Step 2 + 3: Determine even or odd and build the result list
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append("even")
        else:
            result.append("odd")

    return result


# Example run
output = even_odd_list()
print(output)
