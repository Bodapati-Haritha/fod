import nltk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

# Define the customer reviews
reviews = [
    "The product is great and works perfectly.",
    "I am really satisfied with this purchase.",
    "Not happy with the quality. It broke easily.",
    "The customer service was excellent and responsive.",
    "This is the worst product I have ever bought."
]

# Tokenize the reviews and convert to lowercase
words = [word.lower() for review in reviews for word in word_tokenize(review)]

# Calculate word frequencies
word_freq = FreqDist(words)

# Print the frequency distribution
print("Word Frequency Distribution:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
