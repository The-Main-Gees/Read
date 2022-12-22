pos_dict = {
    "N":0,
    "V":1,
    "A":2,
    "J":3,
    "C":4,
    "D":5,
    "P":6,
    "p":7
}

def get_model():
    markov_model = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]
    f = open("markov.txt","r")
    a = f.readlines()
    f.close()
    index = 0
    for i in range(len(markov_model)):
        for j in range(len(markov_model[i])):
            markov_model[i][j] = int(a[index])
            index += 1

    sums = [sum(i) for i in markov_model]
    for i in range(len(markov_model)):
        for j in range(len(markov_model[i])):
            markov_model[i][j] = markov_model[i][j]/sums[i]
    return markov_model

if __name__ == "__main__":
    #train markov model
    '''
    markov_model = [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]]

    gs = open("grammar sequence.txt", "r")
    lines = gs.readlines()
    gs.close()

    for line in lines:
        length = len(line)
        if length <= 2:
            continue
        else:
            line = line[:-1]
            for i in range(length - 2):
                if line[i] == "N":
                    if line[i + 1] == "N":
                        markov_model[0][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[0][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[0][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[0][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[0][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[0][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[0][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[0][7] += 1
                if line[i] == "V":
                    if line[i + 1] == "N":
                        markov_model[1][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[1][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[1][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[1][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[1][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[1][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[1][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[1][7] += 1
                if line[i] == "A":
                    if line[i + 1] == "N":
                        markov_model[2][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[2][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[2][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[2][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[2][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[2][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[2][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[2][7] += 1
                if line[i] == "J":
                    if line[i + 1] == "N":
                        markov_model[3][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[3][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[3][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[3][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[3][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[3][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[3][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[3][7] += 1
                if line[i] == "C":
                    if line[i + 1] == "N":
                        markov_model[4][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[4][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[4][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[4][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[4][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[4][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[4][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[4][7] += 1
                if line[i] == "D":
                    if line[i + 1] == "N":
                        markov_model[5][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[5][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[5][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[5][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[5][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[5][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[5][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[5][7] += 1
                if line[i] == "P":
                    if line[i + 1] == "N":
                        markov_model[6][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[6][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[6][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[6][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[6][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[6][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[6][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[6][7] += 1
                if line[i] == "p":
                    if line[i + 1] == "N":
                        markov_model[7][0] += 1
                    elif line[i + 1] == "V":
                        markov_model[7][1] += 1
                    elif line[i + 1] == "A":
                        markov_model[7][2] += 1
                    elif line[i + 1] == "J":
                        markov_model[7][3] += 1
                    elif line[i + 1] == "C":
                        markov_model[7][4] += 1
                    elif line[i + 1] == "D":
                        markov_model[7][5] += 1
                    elif line[i + 1] == "P":
                        markov_model[7][6] += 1
                    elif line[i + 1] == "p":
                        markov_model[7][7] += 1
    '''

    # store markov model
    '''
    f = open("markov.txt", "w")

    for i in markov_model:
        for j in i:
            f.write(str(j)+"\n")

    f.close()


    '''
    model = get_model()
    for i in model:
        print(*i)