import numpy as np
from operator import itemgetter

# declarando variaveis
valoresFitness   = np.empty((0,3), float)
valoresFitness_n = []
filhos           = []
populacao_nova   = []
populacao        = []
filho            = []
filho2           = []
crossOver_random = 0
resto            = 0
n                = 10

# iniciando uma populacao
populacao        = np.random.randint(5, size=(n,12))
# copiando a populacao
populacao_copia = populacao

#valoresFitness_n = np.random.randint(1,size=(1,3))
#valoresFitness = np.append(valoresFitness, np.array([[1,2,3]]), axis=0)
#valoresFitness = np.append(valoresFitness, np.array([[1,2,4]]), axis=0)
# funcao teste para calculo de apitdao

def calculaApitdaoOrdena(n):
    arr = []
    for x in range(n):
        arr.append([x, np.sum(populacao[x]), 0.0, 0.0])
    arr.sort(key=itemgetter(1), reverse=True)
    return  np.asarray(arr)

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

def crossOver(valoresFitness, porcentagem):
    i

def mutacao(porcentagem):
    a

# retonar uma array ordenado com o valor do fitness de cada
# Individuo da populacao
valoresFitness = calculaApitdaoOrdena(n)

# retonar um array com os valores da roleta
# atualizados
fitnessTotal = roleta(valoresFitness)
print fitnessTotal
print valoresFitness
#valoresFitness[0][2] = 1



'''
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

#print filhos
print ("------")
#print filhos[0]
print ("------")
populacao = np.delete(populacao, (0), axis=0)
#print populacao
print ("------")
np.append(populacao,filhos[0])
#print populacao
'''
