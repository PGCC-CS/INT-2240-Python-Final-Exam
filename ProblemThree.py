# Program that asks the user for words and prints the first letter
# Loop ends when the user enters 0

while True:
    user_input = input("Enter a word (or 0 to stop): ")

    # Exit condition
    if user_input == "0":
        print("Loop ended.")
        break

    # Print the first letter of the word
    print("First letter:", user_input[0])
