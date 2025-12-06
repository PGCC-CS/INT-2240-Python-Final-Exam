def count_letters_digits():
    total_letters = 0
    total_digits = 0

    while True:
        user_input = input("Enter a string (or END to stop): ")

        # Stop condition (any capitalization of END)
        if user_input.lower() == "end":
            break

        # Count letters and digits for this input
        letters = 0
        digits = 0

        for ch in user_input:
            if ch.isalpha():
                letters += 1
            elif ch.isdigit():
                digits += 1

        print(letters, "letters and", digits, "digits")

        # Add to aggregates
        total_letters += letters
        total_digits += digits

    print("Aggregates:", total_letters, "letters and", total_digits, "digits")

# Short main to allow running the function
def main():
    count_letters_digits()

main()