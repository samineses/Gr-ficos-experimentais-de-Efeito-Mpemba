
data = 'Experimento02'
def dados():

    #temperatura ambiente
    label1 = '25°C'
    tempos1 = [0.0, 1.03, 6.13, 12.07, 17.2, 22.37, 28.0, 32.97, 39.03, 45.45, 49.08, 56.43, 62.0]
    temperaturas1 = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]    
    dados01 = [tempos1,temperaturas1,label1]

    label2 = '28°C'
    tempos2 = [0.0, 3.02, 6.33, 12.37, 18.23, 24.17, 31.25, 37.43, 44.0, 49.77, 55.37, 62.37]
    temperaturas2 = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17]
    dados02 = [tempos2,temperaturas2,label2]
    
    dados = [dados01,dados02]
    return dados
    
