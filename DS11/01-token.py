"""
Installera först:
pip install nltk

Testa att punkt fungerar
python -m nltk.downloader 'punkt'
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Exempeltext
text = "Det här är en introduktion till NLP. Det är både spännande och utmanande!"

text2 = "Tokenisering är processen att dela upp en text i mindre enheter som ord, fraser eller meningar. Tokenisering är en viktig del av NLP för att förstå och bearbeta textdata."

nltk.download('punkt', quiet=True)
# Punkt är för att tokenisera text i meningar

nltk.download('punkt_tab', quiet=True)
# Nyare version av punkt, med punkt_tab för att det ska fungera


# Tokenisering
tokens = word_tokenize(text2)

# print("Tokens:", tokens)



nltk.download('stopwords', quiet=True)
swedish_stopwords = set(stopwords.words('swedish'))

filtered_tokens = [word for word in tokens if word.lower() not in swedish_stopwords]
print("Filtrerade tokens:", filtered_tokens)


# Tokens: ['Det', 'här', 'är', 'en', 'introduktion', 'till', 'NLP', '.', 'Det', 'är', 'både', 'spännande', 'och', 'utmanande', '!']

# Text 2:
# tokens: ['Tokenisering', 'processen', 'dela', 'text', 'mindre', 'enheter', 'ord', ',', 'fraser', 'meningar', '.', 'Tokenisering', 'viktig', 'del', 'NLP', 'förstå', 'bearbeta', 'textdata', '.']

