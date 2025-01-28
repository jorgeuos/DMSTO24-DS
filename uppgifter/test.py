from textblob import TextBlob

# Exempeltext
svText = "Jag älskar den här produkten, men leveransen var för långsam."

#  0.0 = Objektiv
#  1.0 = Subjektiv

text = svText

analysis = TextBlob(text)

# Sentimentanalys
print("Polarity:", analysis.sentiment.polarity)
print("Subjectivity:", analysis.sentiment.subjectivity)