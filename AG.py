import numpy as np
from operator import itemgetter

valoresFitness = []
filho  = []
filho2 = []
populacao = np.random.randint(2, size=(5,12))

for x in range(5):
    valoresFitness.append(np.append(x,np.sum(populacao[x])))

print ("----------------------------")
print (" Populacao")
print populacao
print ("----------------------------")
print (" Fitness")
print valoresFitness
print ("----------------------------")
print (" Fitness ordernado")
valoresFitness.sort(key=itemgetter(1), reverse=True)
print valoresFitness
print ("----------------------------")
#print (" Primeiro valor da aptidao")
#print valoresFitness[0][1]
#print valoresFitness[1][1]

if valoresFitness[0][1] == 12:
    print ("Resulado otimo encontrado")
    print valoresFitness[0]

numeroELementos = populacao.size/12

#print valoresFitness[0]
#print valoresFitness[0][0]
#print valoresFitness[0][1]

pai   = populacao[valoresFitness[0][0]]
mae   = populacao[valoresFitness[1][0]]
pai2  = populacao[valoresFitness[2][0]]
mae2  = populacao[valoresFitness[3][0]]
print ("----------------------------")
print ("Crossover")
print ("----------------------------")
#print pai[0]
print ("Pai")
print pai
print ("Aptidao do pai")
print sum(pai)
print ("----------------------------")
print ("Mae")
print mae
print ("Aptidao do pai")
print sum(mae)
print ("----------------------------")
print ("Filho")
filho.append(pai[0])
filho.append(pai[1])
filho.append(pai[2])
filho.append(pai[3])
filho.append(pai[4])
filho.append(pai[5])
filho.append(mae[6])
filho.append(mae[7])
filho.append(mae[8])
filho.append(mae[9])
filho.append(mae[10])
filho.append(mae[11])
print filho
print ("Aptidao do filho")
print sum(filho)
print ("----------------------------")
print ("Filho 2")
filho2.append(mae[0])
filho2.append(mae[1])
filho2.append(mae[2])
filho2.append(mae[3])
filho2.append(mae[4])
filho2.append(mae[5])
filho2.append(pai[6])
filho2.append(pai[7])
filho2.append(pai[8])
filho2.append(pai[9])
filho2.append(pai[10])
filho2.append(pai[11])
print filho2
print ("Aptidao do filho 2")
print sum(filho2)
#populacao.append(filho)
#populacao.append(filho2)
