
data = 'Experimento04'
def dados():

    #temperatura ambiente
    label1 = '28°C_saulo'
    tempos1 = [0.0, 3.23 , 6.06 , 8.40 , 12.15 , 15.25, 19.26, 24.30 , 30.25, 35.28 , 39.28, 45.52]
    temperaturas1 = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17 ]    
    dados01 = [tempos1,temperaturas1,label1]

    label2 = '28°C_matheus'
    tempos2 = [0.0 , 2.10, 5.15, 7.49, 11.13 , 14.34 , 18.38 , 23.44, 28.35, 34.41 , 38.48, 45.06]
    temperaturas2 = [28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18 ,17]    
    dados02 = [tempos2,temperaturas2,label2]
    
    label3 = '35°C_saulo'
    tempos3 = [0.0, 3.30, 5.54, 8.28, 10.50, 14.00, 17.07, 20.18, 24.16, 27.20, 31.47, 36.20, 41.00, 46.07, 50.31]
    temperaturas3 = [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22,21]    
    dados03 = [tempos3,temperaturas3,label3]
    
    
    
    dados = [dados01,dados02,dados03]
    return dados
    
