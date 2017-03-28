import numpy as np

print("iniciando inviduo")
print("-----------------")


populacao = np.random.randint(2, size=(50,12))
print populacao
print "-------------"
print "Individuo 00:"
print populacao[0]
print "-------------"
print "Soma Individuo 00:"
print np.sum(populacao[0])

print "-------------"
print "Individuo 01:"
print populacao[1]
print "-------------"
print "Soma Individuo 01:"
print np.sum(populacao[1])
