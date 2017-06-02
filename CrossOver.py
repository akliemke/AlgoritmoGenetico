import numpy as np

#0.93574297
#0.424382886294
filhos   = np.empty((0,12), int)


def crossOver(valoresFitness, populacao, porcentagem, n):
    selecaoRoleta = []

    for z in range(n):
        n1 = round(np.random.ranf(),8)
        print n1
        for h in range(n):
            if h < 1:
                if n1 > 0 and n1 <= valoresFitness[h][3]:
                    selecaoRoleta.append(valoresFitness[h])
            else:
                if n1 >= valoresFitness[h-1][3] and n1 <=  valoresFitness[h][3]:
                    selecaoRoleta.append(valoresFitness[h])
        if len(selecaoRoleta) == 4:
            break
    selecaoRoleta = np.asarray(selecaoRoleta)
    print ('------')
    print selecaoRoleta
    selecaoRoleta = selecaoRoleta.astype(int)


    for i in range(4):
        if i < 1 or i % 2 == 0:
            filho = []
            crossOver_random = np.random.randint(11)
            resto = 11 - crossOver_random
            for p in range(crossOver_random):
                filho.append(populacao[selecaoRoleta[i][0]][p])
        else:
            for m in range(resto+1):
                va =  crossOver_random + m
                filho.append(populacao[selecaoRoleta[i][0]][va])
    #print np.asarray(filho)
    print ('-------------')
    populacao = np.delete(populacao, (9), axis=0)
    #populacao = np.insert(populacao, np.asarray(filho))
    #print populacao

    return np.asarray(selecaoRoleta)
