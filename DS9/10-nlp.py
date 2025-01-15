from textblob import TextBlob

# Exempeltext
text = "Jag älskar den här produkten, men leveransen var för långsam."
analysis = TextBlob(text)

# Sentimentanalys
print("Polarity:", analysis.sentiment.polarity)
print("Subjectivity:", analysis.sentiment.subjectivity)

# Polarity: 0.5 (positiv ton)
# Subjectivity: 0.6 (ganska subjektiv)

