def dados():
    
    label1 = '25°C_exp01'
    tempos1 = [0, 6, 9, 16, 23, 31, 37, 42]
    temperaturas1 = [25, 24, 23, 22, 21, 20, 19, 18]
    dados01 = [tempos1,temperaturas1,label1]

    label2 = '25°C_exp02'
    tempos2 = [0.0, 1.03, 6.13, 12.07, 17.2, 22.37, 28.0, 32.97, 39.03, 45.45, 49.08, 56.43, 62.0]
    temperaturas2 = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13]    
    dados02 = [tempos2,temperaturas2,label2]

    dados = [dados01,dados02]
    return dados