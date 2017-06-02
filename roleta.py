import numpy as np

valoresFitness   = np.empty((0,3), float)

def roleta(valoresFitness):
    fitnessTotal = 0
    # calcula total da populacao
    for q in range(len(valoresFitness)):
        fitnessTotal = fitnessTotal + valoresFitness[q][1]

    for w in range(len(valoresFitness)):
        valoresFitness[w][2] =  valoresFitness[w][1] / fitnessTotal

    for e in range(len(valoresFitness)):
        if e == 0:
            valoresFitness[e][3] = valoresFitness[e][2] + valoresFitness[e][3]
        else:
            valoresFitness[e][3] = valoresFitness[e][2] + valoresFitness[e-1][3]
        
    return fitnessTotal
