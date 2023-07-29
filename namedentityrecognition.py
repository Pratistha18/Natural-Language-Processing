# Named Entity Recognition

import spacy
# Load the English language model for SpaCy
nlp = spacy.load('en_core_web_sm')

# Sample text
text = "Barack Obama was born in Hawaii. He was the 44th President of the Unites States"
# Proess the text with the SpaCy NLP pipeline
doc = nlp(text)

# Print the named entities in the text
for ent in doc.ents:
    print(ent.text, ent.label_)