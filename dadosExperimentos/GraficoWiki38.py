
data = 'Gráfico Wikipedia com 38 amostragens'
def dados():

    #temperatura ambiente
    label1 = '18,6°C'
    tempos1 = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0, 110.0, 
    120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 
    230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0, 300.0, 310.0, 320.0, 330.0, 
    340.0, 350.0, 360.0, 370.0]
    temperaturas1 = [18.6, 7, 5, 4, 3.5, 2, 1, 0, -1, -2, -2, -3, -3, -3, -3, -4, -4, -5, -5, -6, -6, -7, -7, -7, -7, -8, -8, -9, -9, -9, -10, -10, -10, -10, -10, -10, -10, -10]
    dados01 = [tempos1,temperaturas1,label1]

    label2 = '42,9°C'
    tempos2 = tempos1
    temperaturas2 = [42.9, 38, 34, 30, 27, 24, 21, 19, 17, 15, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -11, -11, -12, -12]
    dados02 = [tempos2,temperaturas2,label2]
    
    dados = [dados01,dados02]
    return dados
    
