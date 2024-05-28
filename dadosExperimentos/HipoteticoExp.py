
data = 'Experimento Hipotetico'

def dados():

    label1 = '25°C'
    tempos1 =       [0, 6, 9, 16, 23, 31, 37, 42, 48.1 , 54.5, 58.1, 65.5, 71.1]
    temperaturas1 = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
    dados01 = [tempos1,temperaturas1,label1]

    label2 = '28°C'
    tempos2 = [0, 3, 6.3333, 12.4, 14.65, 16.9, 19.6166667, 22.6333333, 25.5, 29.9, 33.4, 37.4, 41.4, 45.4, 54.5666667, 62.4, 66.4]
    temperaturas2 = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12]
    dados02 = [tempos2,temperaturas2,label2]

    dados = [dados01,dados02]
    return dados
