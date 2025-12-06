

# Code for question answer
def find_number_index(num_list):
    attempts = 0
    
    while attempts < 3:
        user_input = float(input("Enter a number to search for: "))
        
        if user_input in num_list:
            return num_list.index(user_input)
        else:
            print("Not found")
            attempts += 1
    
    return "Too many failed attempts. Exiting program."

# Code for program run testing:
test_list = [6, 8, 9, 24, 48]
result = find_number_index(test_list)
print("Result:", result)