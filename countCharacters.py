def character_frequency_count(text):
    # Create an empty dictionary to store character frequencies
    char_freq = {}

    # Iterate through each character in the input text
    for char in text:
        # Skip whitespace characters
        if char.isspace(): # we can use char.isdigit() to not count number
            continue

        # Increment the character count in the dictionary
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq

def main():
    # Read in the input string from the user
    text = input("Enter a string: ")
     # we can use this text=text.upper() if want to count small letter the same as capital letter

    # Call the character_frequency_count function to compute the character frequency count
    char_freq = character_frequency_count(text)

    # Sort the dictionary by character count in descending order
    char_freq_sorted = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # Display the character frequency count
    print("Character Frequency Count:")
    for char, count in char_freq_sorted:
        print(f"{count} {char}'s ")
main()
while True:
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y" or play_again == "Y":
        main()
    elif play_again == "n" or play_again == "N":
        break
    else:
        print("Wrong input")
        break

        