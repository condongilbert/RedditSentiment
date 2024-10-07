import nltk
from nltk.tokenize import word_tokenize

# Example text
text = "The stock market is crazy! YOLO and diamond hands are the way to go."

# Tokenization
tokens = word_tokenize(text)
print(tokens)