from urllib.request import urlopen
import re



def pos(token):
    url = 'https://www.merriam-webster.com/dictionary/'
    word = token

    
    try:
        page = urlopen(url+word)
        html = page.read().decode("utf-8")

        pattern1 = '<a class="important-blue-link" href=.*?</a>'
        pattern2 = '<a href=.*? class="cxt">.*?</a>'

        a = re.findall(pattern1, html)
        a2 = re.findall(pattern2, html)
        ans = []
        #remove tags and brackets
        for i in range(len(a)):
            a[i] = re.sub("<.*?>", "", a[i])
            b = re.sub(" \(.*?\)", "", a[i])
            if b not in ans:
                ans.append(b)  

        limit = 3
        new = []
        for val in ans:
            if len(new) == limit:
                break
            if "pronoun" in val:
                new.append('p')
            elif "noun" in val:
                new.append('N')
            elif val == "definite article" or val == "indefinite article":
                new = ['D']
                break
            elif val == "adjective":
                new.append('J')
            elif "adverb" in val:
                new.append('A')
            elif val == "verb" or "verb" in val:
                new.append('V')
            elif val == "preposition":
                new.append('P')
            elif val == "conjunction":
                new.append('C')
        if len(a2) > 0:
            verb_tense = a2[0]
            verb_tense = re.sub("<.*?>", "", verb_tense)
            verb_tense = re.sub(" \(.*?\)", "", verb_tense)
            verb_tense = verb_tense.split(" ")[0]
            new += pos(verb_tense)[0]
    except:
        new = []
    return new
