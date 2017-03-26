import numpy as np

def inicializarIndividuo(tamanho):
    for x in range(0, tamanho):
        print "             We're on time %d" %(x)



print("iniciando inviduo")
print("-----------------")
#inicializarIndividuo(5)

populacao = np.random.randint(2, size=(20,12))
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
