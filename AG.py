import numpy as np
from operator import itemgetter

valoresFitness = []
filhos         = []
populacao_nova = []
populacao      = []
filho          = []
filho2         = []

n = 10

#criando a populao
populacao = np.random.randint(5, size=(n,12))

populacao_copia = populacao
# funcao teste para calculo de apitdao
def calculaApitdaoOrdena(n):
    for x in range(n):
        valoresFitness.append(np.append(x,np.sum(populacao[x])))
    valoresFitness.sort(key=itemgetter(1), reverse=True)

print populacao
print ("------")
calculaApitdaoOrdena(n)

crossOver_random = 0
resto = 0

for i in range(4):
    if i < 1 or i % 2 == 0:
        filho = []
        crossOver_random = np.random.randint(11)
        resto = 11 - crossOver_random
        for p in range(crossOver_random):
            filho.append(populacao[valoresFitness[i][0]][p])
    else:
        for m in range(resto+1):
            va =  crossOver_random + m
            filho.append(populacao[valoresFitness[i][0]][va])

        filhos.append(filho)

print filhos
print ("------")
print filhos[0]
print ("------")
populacao = np.delete(populacao, (0), axis=0)
print populacao
print ("------")
np.append(populacao,filhos[0])
print populacao
