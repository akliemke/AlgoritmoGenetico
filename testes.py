
for x in range(10):
    print x



import numpy as np

valoresFitness = []
populacao = []



populacao = np.random.randint(2, size=(20,12))
print populacao


for x in range(20):
    valoresFitness.append(np.sum(populacao[x]))


#iniciaPopulacao(20)
print ("-----------------")
#fitness(populacao)
print valoresFitness
valoresFitness.sort(reverse=True)
print valoresFitness
