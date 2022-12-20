from itertools import product
import re
import scraper

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

# be, do, have
verbs = ['is', 'am', 'was', 'were', 'are', 'does', 'did', 'has', 'had']

class POS:
    def __init__(self, name):
        self.name = name
        self.description = []
        self.link = None

class Noun(POS):
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.description = []

class Pronoun(Noun):
    pass

class Adjective(POS):
    def __init__(self, name):
        self.name = name
        self.description = []
        self.describes = None

class Verb(POS):
    def __init__(self, name):
        self.name = name
        pass


class Grammar:
    def __init__(self, pos, tokens = None):
        self.pos = "".join(pos)
        self.final = self.pos
        self.size = len(self.pos)
        self.spans = []
        self.span_pos = []
        self.tree_pos = None
        self.tree_token = None
        self.subject = None
        self.verb = None
        self.obj = None

        rules = {
            "DN":"N",
            "JN":"N",
            #"NJ":"N",
            "PN":"J",
            "AV":"V",
            "JJ":"J"
            }

        while True:
            new = None
            for pattern, val in rules.items():
                obj = re.search(pattern, self.final)
                if obj:
                    span = obj.span()
                    self.spans.append(span)
                    self.span_pos.append(val)
                    #new = re.sub(pattern, val, self.temp)
                    new = list(self.final)
                    new[span[0]:span[1]] = val
                    self.final = ''.join(new)
            if new == None:
                break
        val = list(self.pos)
        val2 = list(tokens)
        for span in self.spans:
            v = tuple(val[span[0]:span[1]])
            val[span[0]:span[1]] = ' '
            val[span[0]] = v
            
            v2 = tuple(val2[span[0]:span[1]])
            val2[span[0]:span[1]] = ' '
            val2[span[0]] = v2
        self.tree_pos = tuple(val)
        self.tree_token = tuple(val2)

        # make more general (finding the subject and object)

        #verb
        '''
        v_index = self.final.index('V')
        verb = self.tree_token[v_index]

        if type(verb) is tuple:
            self.verb = ' '.join(verb)
        else:
            self.verb = verb

        #subject
        for i in range(v_index):
            if self.final[i] == 'N' or self.final[i] == 'p':
                subject = self.tree_token[i]
                if type(subject) is tuple:
                    self.subject = ' '.join(subject)
                else:
                    self.subject = subject
                break

        #object
        for i in range(v_index+1, len(self.final)):
            if self.final[i] == 'N' or self.final[i] == 'p':
                obj = self.tree_token[i]
                if type(obj) is tuple:
                    self.obj = ' '.join(obj)
                else:
                    self.obj = obj
                break
    '''
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence.lower()
        self.tokens = self.tokenize()
        self.pos_list = self.POS()
        self.grammar_list = [Grammar(pos, self.tokens) for pos in self.pos_list]

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
            '''
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
            if token in p:
                ans.append('p')
            '''
            ans = scraper.pos(token)
            if token in verbs:
                ans.append('V')
            if ans == []:
                print("No part of speech found for "+token)
                ans.append('N')
            pos_list.append(ans)
        pos = list(product(*pos_list))
        print(len(pos))
        return pos
    
            
    
if __name__ == '__main__':
    val = input()
    sentence = Sentence(val.lower())


    for grammar in sentence.grammar_list:
        #print(grammar.pos)
        print(grammar.final)
        #print(grammar.spans)
        #print(grammar.span_pos)
        print(grammar.tree_token)
        print(grammar.tree_pos)
        #print(grammar.subject)
        #print(grammar.verb)
        #print(grammar.obj)

