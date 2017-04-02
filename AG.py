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

calculaApitdaoOrdena(n)

crossOver_random = 0
resto = 0

for i in range(2):
    if i < 1 or i % 2 == 0:
        crossOver_random = np.random.randint(11)
        resto = 11 - crossOver_random
        #print ("Ponto crossover pai: %d" % crossOver_random )
        #print ("Ponto crossover mae: %d" % resto )
        #print ("pai, valor de i: %d" % i)
        for p in range(crossOver_random):
            #print populacao[valoresFitness[i][0]][p]
            filho.append(populacao[valoresFitness[i][0]][p])
    else:
        #print ("Ponto crossover pai: %d" % crossOver_random )
        #print ("Ponto crossover mae: %d" % resto )
        #print ("mae, valor de i: %d" % i)
        for m in range(resto+1):
            va =  crossOver_random + m
            #print ("Posisao: %d" % va )
            #print ("Item: %d" % populacao[valoresFitness[i][0]][va] )
            filho.append(populacao[valoresFitness[i][0]][va])


filhos.append(filho)

print ("-------------------")


#print ("--------------")
#print ("Primeiro Valor")
#print valoresFitness[0]
print populacao[valoresFitness[0][0]]
#print ("--------------")
#print ("Segundo Valor")
#print valoresFitness[1]
print populacao[valoresFitness[1][0]]
print ("--------------")

print filhos
