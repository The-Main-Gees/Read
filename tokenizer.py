from itertools import product
import re

'''
Problems so far:
1. punctuation marks (especially commas have influence on grammar)
2. Ambiguity of word phrases i.e "I saw him with glasses"
'''

#add more
replace_dict = {
    "isn't" : ["is", "not"],
    "didn't": ["did", "not"],
    "it's": ["it", "is"],
    "i'm": ["i", "am"]
    }

#add more
'''
N -> Noun
V -> Verb
A -> Adverb
J -> Adjective
C -> Conjunction
D -> article
P -> Preposition

N - DN, JN, NJ
J - PN
V - AV
Ultimate form NVN or NV
'''

N = ['i', 'boy', 'he', 'wisdom', 'glasses']
V = ['am', 'is', 'was', 'pushed', 'saw']
D = ['a', 'an', 'the']
J = ['fast', 'tired', 'smart', 'big']
P = ['with', 'on', 'in']

class Grammar:
    def __init__(self, pos):
        self.pos = "".join(pos)
        self.temp = self.pos
        self.size = len(self.pos)
        self.spans = []
        self.span_pos = []
        self.final = None

        rules = {
            "DN":"N",
            "JN":"N",
            "NJ":"N",
            "PN":"J",
            "AV":"V"
            }

        while True:
            new = None
            for pattern, val in rules.items():
                obj = re.search(pattern, self.temp)
                if obj:
                    span = obj.span()
                    self.spans.append(span)
                    self.span_pos.append(val)
                    #new = re.sub(pattern, val, self.temp)
                    new = list(self.temp)
                    new[span[0]:span[1]] = val
                    self.temp = ''.join(new)
            if new == None:
                break
        val = list(self.pos)
        for span in self.spans:
            v = tuple(val[span[0]:span[1]])
            val[span[0]:span[1]] = ' '
            val[span[0]] = v
        self.final = tuple(val)
                      

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.tokens = self.tokenize()
        self.pos_list = self.POS()
        self.grammar_list = [Grammar(pos) for pos in self.pos_list]

    def tokenize(self):
        first_tokens = self.sentence.split(" ")

        for index in range(len(first_tokens)):
            if first_tokens[index] in replace_dict:
                first_tokens.insert(index+1 , replace_dict[first_tokens[index]][1])
                first_tokens[index] = replace_dict[first_tokens[index]][0]

        return(first_tokens)

    def POS(self):
        pos_list = []
        for token in self.tokenize():
            ans = []
            # search each part of speech file and add the part of speech to ans list if found
            if token in N:
                ans.append('N')
            if token in V:
                ans.append('V')
            if token in D:
                ans.append('D')
            if token in J:
                ans.append('J')
            if token in P:
                ans.append('P')
            if ans == []:
                print("No part of speech found for "+token)
            pos_list.append(ans)
        pos = list(product(*pos_list))
        return pos
    
            
    

val = input()
sentence = Sentence(val.lower())


for grammar in sentence.grammar_list:
    print(grammar.pos)
    print(grammar.temp)
    print(grammar.spans)
    print(grammar.span_pos)
    print(grammar.final)

