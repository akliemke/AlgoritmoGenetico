import numpy as np
import time
from operator import itemgetter 
# necessario para suprimir a notacao
np.set_printoptions(suppress=True)
print("iniciando inviduo")
print("-----------------")

custos = [8, 12, 17]
kilometros_viagens = [500.0, 200.0, 55.0]
cidade_saida   = [111, 222, 333]
cidade_destino = [444, 555, 666]

#a = np.zeros(shape=(3,3))
#b = np.zeros(shape=(3,3))

#a[0][0] = 1
#a[0][2] = 1
#a[1][1] = 1
#a[2][0] = 1
#a[2][2] = 1

#b[0][2] = 1
#b[1][1] = 1
#b[1][1] = 0
#b[2][0] = 1
#b[2][1] = 1
#b[2][2] = 1
#c = a * b
#print a
#print("-----------------")
#print b
#print("-----------------")
#print c
populacao = []
#individuo = np.random.randint(2, size=(3,12))
#individuo2 = np.random.randint(2, size=(3,12))


individuo  = np.zeros(shape=(3,8))
individuo2 = np.zeros(shape=(3,8))



populacao.append(individuo)
populacao.append(individuo2)
populacao = np.asarray(populacao)


#print populacao


#print type(populacao)
#print populacao

#print "-------------"
#print populacao

for indivi in range(2):
    for viagem in range(3):
        for parametro in range(8):
            if parametro == 0: # Dia da viagem
                populacao[indivi][viagem][parametro] = time.strftime("%d")
            if parametro == 1: # Cidade Partida
                populacao[indivi][viagem][parametro] = cidade_destino[viagem]
            if parametro == 2: # Cidade Destino
                populacao[indivi][viagem][parametro] = cidade_saida[viagem]
            if parametro == 3: # Km's viagem
                populacao[indivi][viagem][parametro] = kilometros_viagens[viagem]
            if parametro == 4:
                populacao[indivi][viagem][parametro] = np.random.randint(3)
            if parametro == 5: # Perido que a viagem sera realizada
                populacao[indivi][  viagem][parametro] = np.random.randint(3)
            if parametro == 6: # Numero do carro
                populacao[indivi][viagem][parametro] = np.random.randint(3)
            if parametro == 7: # Custo da viagem
                populacao[indivi][viagem][parametro] = custos[int(populacao[indivi][viagem][6])] * populacao[indivi][viagem][3]

                # = custos[int(populacao[indivi][viagem][6])] * int(populacao[indivi][viagem][3])
                #print custos[int(populacao[indivi][viagem][6])]
                #print populacao[indivi][viagem][3]

            #print populacao[indivi][viagem][parametro]
#custos[]
#int(populacao[indivi][viagem][7])
#print "-------------"
#print type()
#x = 1.0
#y = 100000.0
#print '%f' % (15.5 * 500)
#print (15.5 * 500)
print populacao
soma =  np.sum(populacao[0], axis=0)
arr = []
for x in range(2):
    soma =  np.sum(populacao[x], axis=0)
    arr.append([x, soma[7], 0.0, 0.0])
arr.sort(key=itemgetter(1), reverse=True)

print arr
print "-------------"
print soma[7]
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
