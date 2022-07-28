import nltk

replace_dict = {
    "isn't" : ["is", "not"],
    "didn't": ["did", "not"],
    "it's": ["it", "is"],
    "i'm": ["i", "am"]
    }

def tokenize(sentence):
    first_tokens = sentence.split(" ")

    for index in range(len(first_tokens)):
        if first_tokens[index] in replace_dict:
            first_tokens.insert(index+1 , replace_dict[first_tokens[index]][1])
            first_tokens[index] = replace_dict[first_tokens[index]][0]

    print(first_tokens)

val = input()
tokenize(val.lower())
