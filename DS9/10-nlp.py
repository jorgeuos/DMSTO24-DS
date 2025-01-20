from textblob import TextBlob

# Exempeltext
svText = "Jag älskar den här produkten, men leveransen var för långsam."
enText = "I love this product, but the delivery was too slow."
enText2 = "This product is 10 feet long and 2 inches wide."
#  0.0 = Objektiv
#  1.0 = Subjektiv

text = enText2

analysis = TextBlob(text)

# Sentimentanalys
print("Polarity:", analysis.sentiment.polarity)
print("Subjectivity:", analysis.sentiment.subjectivity)


