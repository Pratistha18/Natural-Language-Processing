#Chunking
import nltk

sentence = "the little yellow dog barked at the cat"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(pos_tags)
tree = nltk.tree.Tree.fromstring(str(result))
tree.pretty_print()
