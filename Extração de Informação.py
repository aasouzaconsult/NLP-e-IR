# http://www.nltk.org/book/ch07.html

locs = [( 'Omnicom' , 'IN' , 'New York' ),
        ( 'DDB Needham' , 'IN' , 'New York' ),
        ( 'Kaplan Thaler Group' , 'IN' , 'New York' ),
        ( 'BBDO Sul' , 'IN' , 'Atlanta' ),
        ( 'Georgia-Pacific' , 'IN' , 'Atlanta' )]
query = [e1 for (e1, rel, e2) in locs if e2=='Atlanta']
print (query)
##################################################################

import nltk
groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
   'shot' -> 'I' | 'elephant' | 'in'
   'elephant' -> 'an' | 'in'
   'in' -> 'pajamas'
   'pajamas' -> 'my'
""")
print(groucho_dep_grammar)
pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
for tree in trees:
   print(tree)

################################################################## 
# Chunking (grafico)

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")] 

grammar = "NP: {<DT>?<JJ>*<NN>}" # Esta regra diz que um pedaço NP deve ser formado quando o 
#chunker encontra um determinador opcional (optional determiner) ( DT ), seguido por qualquer número de adjetivos ( JJ) 
#e, em seguida, um substantivo ( NN ).

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
result.draw()
