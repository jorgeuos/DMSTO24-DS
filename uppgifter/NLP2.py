from textblob import TextBlob

text = "I love this product, but the delivery was too slow."
analysis = TextBlob(text)
print("Polarity:", analysis.sentiment.polarity)
print("Subjectivity:", analysis.sentiment.subjectivity)
