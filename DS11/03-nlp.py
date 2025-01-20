from textblob import TextBlob

svTexts = [
   "Den här produkten är fantastisk!",
   "Jag är missnöjd med servicen.",
   "Helt okej upplevelse, inte mer."
]

enTexts = [
    "This product is amazing!",
    "I am dissatisfied with the service.",
    "Okay experience, nothing more."
]

texts = enTexts

for text in texts:
   analysis = TextBlob(text)
   print(f"Text: {text}")
   print(f"Polarity: {analysis.sentiment.polarity}")
   print(f"Subjectivity: {analysis.sentiment.subjectivity}\n")



