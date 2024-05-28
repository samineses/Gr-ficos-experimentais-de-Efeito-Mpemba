import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def logica(data,dados,intersec):

    # Criando o gráfico
    plt.figure(figsize=(10, 6))

    # Plotando os conjuntos de dados através de um dicionário
    dados_dict = {}
    grausList = []
    temposList = []
    #grausList = [max(dados01[1]),min(dados01[1]),max(dados02[1]),min(dados02[1])]
    #temposList = [max(dados01[0]),max(dados02[0])]

    for i in range(len(dados)):
        key = f'dados{i+1:02d}'
        dados_dict[key] = dados[i]
        plt.plot(dados_dict[key][0], dados_dict[key][1], marker='o', linestyle='-', label=dados_dict[key][2])
        grausList.extend([max(dados_dict[key][1]), min(dados_dict[key][1])])
        temposList.append(max(dados_dict[key][0]))


    '''
    # Estimando um initial_guess genérico
    initial_guess = (np.mean(dados[0][0]), np.mean([np.interp(np.mean(dados[0][0]), dados[0][0], dados[0][1]), np.mean(dados[0][1])]))


    # Função que retorna a diferença entre as duas curvas para encontrar a interseção
    def diff_equation(point):
        x, y = point
        return (np.interp(x, dados01[0], dados01[1]) - y, np.interp(x, dados02[0], dados02[1]) - y)

    
    #Encontrar e  Desenhar o Ponto de Interseção e a Sua Reta horizontal
    if(intersec == 1):
        intersection_point = fsolve(diff_equation, initial_guess)
        #plt.scatter(*intersection_point, color='green', label='Ponto de Interseção')
        plt.axhline(y=intersection_point[1], color='green', linestyle='--', label='Reta Horizontal Passando pela Interseção')
    '''
    plt.axhline(y=0, color='green', linestyle='-', label='origem')
    plt.axhline(y=42.9, color='green', linestyle='--', label='r1')
    plt.axhline(y=18.6, color='green', linestyle='--', label='r2')


    #Deslocando o eixo y para a posição x=0
    ax = plt.gca()
    ax.spines['left'].set_position(('data', 0))

    # Adicionando título e rótulos
    title = 'Resfriamento ao longo do tempo\n'+data
    plt.title(title)
    plt.xlabel('Tempo (minutos)')
    plt.ylabel('Temperatura (°C)')

    # Adicionando grid e legendas
    plt.grid(True)
    plt.legend(loc='upper right',fontsize=7)

    
    # Definindo os ticks dos eixos    
    '''
    if(len(dados)==4):
        grausList.extend([max(dados03[1]),min(dados03[1])])
        grausList.extend([max(dados04[1]),min(dados04[1])])
        temposList.append(max(dados03[0]))
        temposList.append(max(dados04[0]))
    '''

    maxGrau = int(max(grausList))+4
    minGrau = int(min(grausList))-4
    maxTempo = int(max(temposList))
    
    plt.yticks(range(minGrau, maxGrau, 2))
    plt.xticks(range(0, maxTempo, 5))

    #plt.xticks(range(0, 80, 5))
    #plt.yticks(range(10, 50, 2))

    # Exibindo o gráfico
    plt.show()
    
    return

