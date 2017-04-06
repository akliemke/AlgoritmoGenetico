import numpy as np
from operator import itemgetter

def calculaApitdaoOrdena(n, populacao):
    arr = []
    for x in range(n):
        arr.append([x, np.sum(populacao[x]), 0.0, 0.0])
    arr.sort(key=itemgetter(1), reverse=True)
    return  np.asarray(arr)
