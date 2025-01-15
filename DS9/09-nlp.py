import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')
swedish_stopwords = set(stopwords.words('swedish'))

filtered_tokens = [word for word in tokens if word.lower() not in swedish_stopwords]
print("Filtrerade tokens:", filtered_tokens)

# Filtrerade tokens: ['introduktion', 'NLP', '.', 'spännande', 'utmanande', '!']
