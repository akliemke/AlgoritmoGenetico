import numpy as np
from operator import itemgetter

def calculaApitdaoOrdena(n, populacao):
    arr = []
    for x in range(n):
        soma =  np.sum(populacao[x], axis=0)
        arr.append([x, soma[7], 0.0, 0.0, 0.0])
    arr.sort(key=itemgetter(1), reverse=True)

    valoresFitness = np.asarray(arr)

    for n in range(x+1):
        valoresFitness[n][2] = valoresFitness[n][1] * (n+1)

            

    return  valoresFitness
