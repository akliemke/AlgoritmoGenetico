import numpy as np

populacao        = []


def criaPopulacao(n):
    # iniciando uma populacao
    populacao        = np.random.randint(5, size=(n,12))
    return populacao
