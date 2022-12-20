from tokenizer import *

class Dynamic:
    def __init__(self, name):
        '''
        self.name = []
        self.age = []
        self.gender = []
        self.color = []
        self.attributes = []
        '''
        self.name = name
        self.category = None
        self.actions = []

    def action(self, action, other):
        self.actions.append((action, other))
        other.actions.append((self, action))

    def print_action(self, index):
        action = self.actions[index]
        if type(action[0]) is str:
            print(self.name, action[0], action[1].name)
        else:
            print(self.name, action[1], "by", action[0].name)
    '''
    def search(self, verb = None, name=None):
        #name
        if verb == None and name!= None:
            for pair in self.actions:
                #index 0 is the same
    '''

    def list_actions(self, index):
        actions_verbs = []
        for pair in self.actions:
            if type(pair[0]) == str:
                action_verbs.append(pair[0])
            else:
                pass




def main():
    val = input()
    sentence = Sentence(val)
    '''
    for grammar in sentence.grammar_list:
        s = Dynamic(grammar.subject)
        o = Dynamic(grammar.obj)
        s.action(grammar.verb, o)
        s.print_action(0)
        o.print_action(0)
    '''

    grammar = sentence.grammar_list[0]
    
    
if __name__ == '__main__':

    data = []
    

    
