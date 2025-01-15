"""
Installera först:
pip install nltk

Testa att punkt fungerar
python -m nltk.downloader 'punkt'

"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk.download()

# Exempeltext
text = "Det här är en introduktion till NLP. Det är både spännande och utmanande!"

nltk.download('punkt')

# Tokenisering
tokens = word_tokenize(text)

print("Tokens:", tokens)



nltk.download('stopwords')
swedish_stopwords = set(stopwords.words('swedish'))

filtered_tokens = [word for word in tokens if word.lower() not in swedish_stopwords]
print("Filtrerade tokens:", filtered_tokens)

# Tokens: ['Det', 'här', 'är', 'en', 'introduktion', 'till', 'NLP', '.', 'Det', 'är', 'både', 'spännande', 'och', 'utmanande', '!']

