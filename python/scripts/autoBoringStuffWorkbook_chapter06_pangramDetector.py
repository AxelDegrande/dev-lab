def is_pangram(sentence):
    EACH_LETTER = []

    sentence = "".join(sentence.split()) # Remove all whitespace from sentence
    sentence = sentence.lower() # Transform sentence to only lower-case letters

    for letter in sentence:
        if letter not in EACH_LETTER:
            EACH_LETTER.append(letter)

    if len(EACH_LETTER) == 26:
        isPangram = True
    else:
        isPangram = False

    return isPangram    

sentence = "The quick brown fox jumps over the yellow lazy dog"
result = is_pangram(sentence)

print("The senctence is a pangram: " + str(result))
