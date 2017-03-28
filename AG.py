import numpy as np
from operator import itemgetter

arrayTipos = [('index', int), ('fitness', int)]
valoresFitness = []
populacao  = []



populacao = np.random.randint(2, size=(5,12))
print populacao


for x in range(5):
    valoresFitness.append(np.append(x,np.sum(populacao[x])))


print ("-----------------")
print valoresFitness
valoresFitness.sort(key=itemgetter(1), reverse=True)
print valoresFitness
