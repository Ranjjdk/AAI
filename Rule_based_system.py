# Write a program for to implement Rule based system.

import spacy 
from spacy.matcher import Matcher
nlp=spacy.load('en_core_web_sm')
matcher=Matcher(nlp.vocab) 
doc = nlp("New IPhone X is released")
pattern=[{'ORTH':'New'}, {'ORTH':'IPhone'}]
matcher.add('Iphone_pattern',[pattern])
matches = matcher(doc) 
for match_id, start, end in matches:
 matched_span = doc[start:end] 
print(matched_span.text)


doc = nlp("2020 Fifa World Cup : India Wins")
pattern=[{'IS_DIGIT':True},{'LOWER':'fifa'}, {'LOWER':'world'}, {'LOWER':'cup'}, {'IS_PUNCT':True}]
matcher.add('FIFA_PATTERN',[pattern])
matches = matcher(doc) 
for match_id, start, end in matches:
 matched_span = doc[start:end] 
print(matched_span.text,"\n")
doc = nlp("I love chocolates but now I loving icecreams more") 
pattern=[{'LEMMA':'love'}, {'POS':'NOUN'}] 
matcher.add('EAT_PATTERN',[pattern]) 
matches = matcher(doc) 
for match_id, start, end in matches: 
 matched_span = doc[start:end] 
print(matched_span.text)
doc = nlp("I bought smartphone now I am buying another smartphone") 
pattern=[{'LEMMA':'buy'}, {'POS':'DET', "OP":'?'}, {'POS':'NOUN'}] 
matcher.add('EA_PATTERN',[pattern]) 
matches = matcher(doc) 
for match_id, start, end in matches: 
 matched_span = doc[start:end] 
print(matched_span.text) 
