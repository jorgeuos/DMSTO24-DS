import spacy
"""
Installera först:
pip install spacy
"""


# Ladda svensk NLP-modell
nlp = spacy.load("sv_core_news_sm")

# Exempeltext
doc = nlp("Google grundades av Larry Page och Sergey Brin i USA.")

# Identifiera entiteter
for ent in doc.ents:
   print(ent.text, ent.label_)

