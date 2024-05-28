
data = 'Experimento01'
def dados():

    #temperatura ambiente e tempos convertidos em minutos decimais
    label1 = '25°C'
    tempos1 = [0, 6, 9, 16, 23, 31, 37, 42]
    temperaturas1 = [25, 24, 23, 22, 21, 20, 19, 18]
    dados01 = [tempos1,temperaturas1,label1]

    label2 = '28°C'
    tempos2 = [0.0, 2.42, 4.5, 7.22, 10.23, 13.1, 17.5, 21.0, 25.0, 29.0, 33.0, 42.17, 50.0, 54.0]
    temperaturas2 = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]
    dados02 = [tempos2,temperaturas2,label2]
    
    dados = [dados01,dados02]
    return dados
    
