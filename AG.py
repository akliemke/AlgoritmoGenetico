import numpy as np
from operator import itemgetter

valoresFitness = []
filho  = []
filho2 = []

n = 5
populacao = np.random.randint(2, size=(n,12))

# funcao teste para calculo de apitdao
def calculaApitdao(n):
    for x in range(n):
        valoresFitness.append(np.append(x,np.sum(populacao[x])))
    valoresFitness.sort(key=itemgetter(1), reverse=True)
    return valoresFitness

#def selecao(populacao, valoresFitness):


print populacao

calculaApitdao(n)
print valoresFitness
