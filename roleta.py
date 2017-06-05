import numpy as np

valoresFitness   = np.empty((0,4), float)

def roleta(valoresFitness):
    fitnessTotal = 0
    # calcula total da populacao
    for q in range(len(valoresFitness)):
        fitnessTotal = round(fitnessTotal + valoresFitness[q][2],2)

    for w in range(len(valoresFitness)):
        valoresFitness[w][3] =  round(valoresFitness[w][2] / fitnessTotal,2)

    for e in range(len(valoresFitness)):
        if e == 0:
            valoresFitness[e][4] = round(valoresFitness[e][3] + valoresFitness[e][4],2)
        else:
            valoresFitness[e][4] = round(valoresFitness[e][3] + valoresFitness[e-1][4],2)

    return fitnessTotal
