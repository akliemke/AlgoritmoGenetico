import numpy as np
from operator import itemgetter

valoresFitness = []
populacao_nova = []
populacao      = []
filho          = []
filho2         = []

n = 10

populacao = np.random.randint(5, size=(n,12))

# funcao teste para calculo de apitdao
def calculaApitdaoOrdena(n):
    for x in range(n):
        valoresFitness.append(np.append(x,np.sum(populacao[x])))
    valoresFitness.sort(key=itemgetter(1), reverse=True)

print populacao

calculaApitdaoOrdena(n)
print valoresFitness

for i in range(n):
    print populacao[valoresFitness[i][0]]
    print populacao[valoresFitness[i][0]]
    print populacao[valoresFitness[i][0]][0]
    print valoresFitness[i][1]
