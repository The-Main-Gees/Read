import spacy
sp = spacy.load('en_core_web_sm')
text = input("")
sentence = sp(text)
for word in sentence:
    print(word.pos_)