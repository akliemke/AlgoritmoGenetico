import numpy as np

from criaPopulacao          import criaPopulacao
from calculaAptidaoOrdenada import calculaApitdaoOrdena
from roleta                 import roleta
from CrossOver              import crossOver
from Mutacao                import mutacao

tamanhoPopulacao = 10

populacao      = criaPopulacao(tamanhoPopulacao)
valoresFitness = calculaApitdaoOrdena(tamanhoPopulacao, populacao)
fitnessTotal   = roleta(valoresFitness)
print valoresFitness
filhos = crossOver(valoresFitness, populacao, 0, tamanhoPopulacao)

#populacao = crossOver(valoresFitness, populacao, 0, tamanhoPopulacao)




print populacao
