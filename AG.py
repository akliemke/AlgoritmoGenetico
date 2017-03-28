import numpy as np
from operator import itemgetter

arrayTipos = [('index', int), ('fitness', int)]
valoresFitness = []
populacao  = []
numeroElementos = 0
pai = []
mae = []
populacao = np.random.randint(2, size=(5,12))

for x in range(5):
    valoresFitness.append(np.append(x,np.sum(populacao[x])))

print ("-----------------")
print (" Populacao")
print populacao
print ("-----------------")
print (" Fitness")
print valoresFitness
print ("-----------------")
print (" Fitness ordernado")
valoresFitness.sort(key=itemgetter(1), reverse=True)
print valoresFitness
print ("-----------------")
print (" Primeiro valor da aptidao")
print valoresFitness[0][1]

if valoresFitness[0][1] == 12:
    print ("Resulado otimo encontrado")
    print valoresFitness[0]

numeroELementos = populacao.size/12

print valoresFitness[0]
print valoresFitness[0][0]
print valoresFitness[0][1]
#for x in range(numeroElementos):
