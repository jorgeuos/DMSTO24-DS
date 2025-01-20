import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import stopwords


# Exempeltext
text = "Det här är en introduktion till NLP. Det är både spännande och utmanande!"

nltk.download('punkt')
nltk.download('punkt_tab')

# Tokenisering
tokens = word_tokenize(text)


nltk.download('stopwords')
swedish_stopwords = set(stopwords.words('swedish'))

filtered_tokens = [word for word in tokens if word.lower() not in swedish_stopwords]
print("Filtrerade tokens:", filtered_tokens)

# Filtrerade tokens: ['introduktion', 'NLP', '.', 'spännande', 'utmanande', '!']
