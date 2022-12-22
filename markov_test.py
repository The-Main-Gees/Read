import tokenizer
import time
start = time.time()
passage = []
count = 0

af = open("animal farm.txt", "r")
count = int(af.read(4))
af.read(1)
s = []
i = 0
while i < count:
    b = af.read(1)
    #print(b)
    if b == "\n":
        s.append(" ")
    elif b == "." or b == "?" or b == "!":
        af.read(1)
        passage.append("".join(s))
        s = []
        i += 1
    else:
        s.append(b)

af.close()

f = open("grammar sequence.txt", "r")

ans = f.readlines()

f.close()

c = 0
plus = 0
for i in range(count):
    if ans[i] == "\n":
        continue
    else:
        m = tokenizer.use_model(passage[i])
        a = ans[i]
        a = a[:-1]
        A = len(a)
        M = len(m)
        if A != M:
            continue
        for j in range(len(a)):
            if a[j] == m[j]:
                plus += 1
            elif (a[j] == 'p' and m[j] == 'N') or (a[j] == 'N' and m[j] == 'p'):
                plus += 1
            c += 1
        if a != m:
            print(a, m, passage[i])
print(plus/c)
end = time.time()
print(end-start)