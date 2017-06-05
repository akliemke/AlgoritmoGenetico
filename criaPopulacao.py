import numpy as np
import time
np.set_printoptions(suppress=True)


custos = [8, 12, 17]
kilometros_viagens = [500.0, 200.0, 55.0, 900.0]
cidade_saida   = [111, 222, 333, 777]
cidade_destino = [444, 555, 666,888]


def criaPopulacao(tamanhoPopulacao, numeroViagens):
    populacao        = []
    # Cria os individuo a partir do numero de viagens
    for x in range(tamanhoPopulacao):
        populacao.append(np.zeros(shape=(numeroViagens,8)))

    populacao = np.asarray(populacao)

    # iniciando uma populacao
    for indivi in range(tamanhoPopulacao):
        for viagem in range(numeroViagens):
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

    return populacao
