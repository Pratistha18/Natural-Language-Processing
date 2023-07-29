# Probabilistic context-free grammar using the NLTK library in Python, and then uses the PCFG to parse a sentence

from nltk.parse import pchart
from nltk import PCFG

# Define the grammar rules
grammar = PCFG.fromstring("""
                          S -> NP VP [1.0]
                          PP -> P NP [0.4] | P NP PP [0.6]
                          NP -> Det N1 [0.6] | Det N1 PP [0.4]
                          VP -> V NP [0.7] | V NP PP [0.3]
                          Det -> 'the' [0.5] | 'a' [0.5]
                          N1 -> 'dog' [0.1667] | 'cat'[0.1667] | 'bird' [0.1667] | 'man' [0.1667] | 'woman' [0.1666] | 'mat' [0.1666]
                          V -> 'chased' [0.3] | 'sat' [0.3] | 'ate' [0.4]
                          P -> 'on' [0.2] | 'in' [0.3] | 'by' [0.5]
                          """)
# Create a parser
parser = pchart.InsideChartParser(grammar)
# Define a sentence to parse
sentence = "the dog chased the cat on the mat".split()
# Parse the sentence and print the results
for tree in parser.parse(sentence):
    print(tree)
tree.pretty_print()