def frequency(text):
    charFreq = {}

    for char in text:
        if char.isspace():
            continue

        if char in charFreq:
            charFreq[char] += 1
        else:
            charFreq[char] = 1

    return charFreq

text = input("Please enter the sentence")
text = text.upper()

charFreq = frequency(text)

charFreqSorted = sorted(charFreq.items(), key=lambda x: x[1], reverse=True)

print("Character's frequency:")
for char, count in charFreqSorted:
    print(f"{count} {char}'s ")