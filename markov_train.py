#load a file for the sentences.
#tokenize for sentences.
#tokenize for words.
#skip senetences with punctuation marks
#load second file for values
#crate markov table
#test markov table

import string
from tokenizer import Sentence

passage = []
count = 0
length = 168556

af = open("animal farm.txt", "r")
count = int(af.read(4))
af.read(1)
s = []
i = 0
while i < length-2:
    b = af.read(1)
    #print(b)
    i+=1
    if b == "\n":
        s.append(" ")
    elif b == "." or b == "?" or b == "!":
        af.read(1)
        i+=1
        passage.append("".join(s))
        s = []
    else:
        s.append(b)

af.close()


new_count = count
gs = open("grammar sequence.txt", "a")

for line in passage[count:]:
    next = True
    for char in line:
        if char in string.punctuation:
            gs.write("\n")
            new_count += 1
            next = False
            break
        else:
            pass
    if next:
        print(new_count)
        s = Sentence(line)
        t = s.tokenize()
        print(t)
        ans = input()
        gs.write(ans+"\n")
        new_count += 1
gs.close()
