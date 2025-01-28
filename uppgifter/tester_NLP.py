import nltk
from nltk.tokenize import word_tokenize
# Exempeltext
text = "Det här är en introduktion till NLP. Det är både spännande och utmanande!"
nltk.download('punkt')
# Tokenisering
tokens = word_tokenize(text)
print("Tokens:", tokens)


# Tokens: ['Det', 'här', 'är', 'en', 'introduktion', 'till', 'NLP', '.', 'Det', 'är', 'både',
# 'spännande', 'och', 'utmanande', '!']