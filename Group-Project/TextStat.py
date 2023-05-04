import string
import unicodedata
from collections import Counter

#def compute_word_frequency(text):


#def compute_char_frequency(text):


#def display_word_frequency(word_freq):


#def display_char_frequency(char_freq):


def display_statistical_information(text):
    """Displays statistical information about the text."""
    lines = text.count('\n') + 1
    words = len(text.split())
    chars = len(text)
    print("ቁጥራዊ መርጃ(Statistical Information):")
    print()
    print(f"ጠቅላላ መስመር(Total Lines): {lines}")
    print()
    print(f"ጠቅላላ የቃላት ብዛት(Total Words): {words}")
    print()
    print(f"ጠቅላላ የፊደል ብዛት(Total Characters): {chars}")

    
 

# Read text file
#we can read both amaharic and English Text
with open("C:/Users/hm/Dropbox/My PC (LAPTOP-6M4OIP3C)/Desktop/AI project/Group-project/amharic.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Remove special characters and normalize Amharic characters
text = "".join([char for char in text if char not in string.punctuation])
text = unicodedata.normalize('NFKD', text)

#word frequency
word_freq = compute_word_frequency(text)

# character frequency
char_freq = compute_char_frequency(text)

# Display word frequency
display_word_frequency(word_freq)

# Display character frequency
display_char_frequency(char_freq)

# Display statistical information
display_statistical_information(text)
