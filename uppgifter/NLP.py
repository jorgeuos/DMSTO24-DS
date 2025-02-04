import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')
swedish_stopwords = set(stopwords.words('swedish'))

tokens = ['Detta', 'är', 'en', 'introduktion', 'till', 'NLP', '.', 'Det', 'är', 'spännande', 'och', 'utmanande', '!']

filtered_tokens = [word for word in tokens if word.lower() not in swedish_stopwords]
print("Filtrerade tokens:", filtered_tokens)

# Filtrerade tokens: ['introduktion', 'NLP', '.', 'spännande', 'utmanande', '!']