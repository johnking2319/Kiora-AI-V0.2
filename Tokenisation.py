#Tokenisation
text = input("Enter text: ")

tokens = []
current_word = ""

# Tokenize words and special characters
for char in text:

    if char == " " or char == "\t" or char == "\n" or char == "\r" or char == "\v" or char == "\f":

        if current_word:
            tokens.append(current_word)
            current_word = ""

    else:
        current_word += char

# Add the last word
if current_word:
    tokens.append(current_word)


# Create vocabulary and token IDs
vocabulary = {}
token_ids = []
cur_id = 0

for token in tokens:

    if token not in vocabulary:
        vocabulary[token] = cur_id
        cur_id += 1

    token_ids.append(vocabulary[token])


# Display results
print("\nTokens:", tokens)
print("\nVocabulary:", vocabulary)
print("\nToken IDs:", token_ids)