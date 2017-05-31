import numpy as np

print("iniciando inviduo")
print("-----------------")

custos = [12.5, 14.0, 10]




populacao = []
#individuo = np.random.randint(2, size=(3,12))
#individuo2 = np.random.randint(2, size=(3,12))


individuo  = np.zeros(shape=(3,12))
individuo2 = np.zeros(shape=(3,12))



populacao.append(individuo)
populacao.append(individuo2)
populacao = np.asarray(populacao)





#print type(populacao)
#print populacao

print "-------------"
populacao[0][0][11] = 100.0
populacao[0][1][11] = 200.0
populacao[0][2][11] = 300.0

populacao[1][0][11] = 400.0
populacao[1][1][11] = 500.0
populacao[1][2][11] = 600.0

print populacao

for indivi in range(2):
    for viagem in range(3):
        for parametro in range(12):
            print populacao[indivi][viagem][parametro]

#print populacao[0]
#print "-------------"
#print populacao[0][0]
#print "-------------"
#print populacao[0][0][0]
#print individuo
#print "-------------"
#print "Individuo 00:"
#print individuo [0]
#print "-------------"
#print "Soma Individuo 00:"
#print np.sum(individuo [0])

#print "-------------"
#print "Individuo 01:"
#print individuo [1]
#print "-------------"
#print "Soma Individuo 01:"
#print np.sum(individuo [1])
